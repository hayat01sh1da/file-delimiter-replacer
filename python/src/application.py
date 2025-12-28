import glob
import inspect
import os
import re
import shutil

class InvalidModeError(Exception):
    pass

class Application:
    def __init__(self, extension = None, delimiter = '_', mode = 'd'):
        self.extension           = extension
        self.delimiter           = delimiter
        self.mode                = mode
        self.paths               = glob.glob(os.path.join('.', '**', f'*{extension or ''}'), recursive = True)
        self.exec_mode           = self.__exec_mode__()
        self.env                 = inspect.stack()[1].filename.split('/')[-2]
        self.file_conversion_map = self.__file_conversion_map__()

    def run(self):
        self.__validate__(self.mode)
        self.__replace__()

    # private

    def __validate__(self, mode):
        """Validate the provided mode is either 'd' (dry-run) or 'e' (execution).

        Args:
            mode: The mode to validate.

        Raises:
            InvalidModeError: If mode is not 'd' or 'e'.
        """
        match mode:
            case 'd' | 'e':
                return
            case _:
                raise InvalidModeError(f'{self.mode} is invalid mode. Provide either `d`(default) or `e`.')

    def __replace__(self):
        """Replace delimiters in file paths.
        
        Returns:
            None
        """
        self.__output__(f'Target extension is `{self.extension}`')

        if not self.paths:
            self.__output__(f'========== [{self.exec_mode}] No `{self.extension}` files found ==========')
            return

        self.__output__(f'========== [{self.exec_mode}] Total File Count to Clean: {len(self.paths)} ==========')
        self.__output__(f'========== [{self.exec_mode}] The delimiters of those files will be replaced with `{self.delimiter}` ==========')
        self.__output__(f'========== [{self.exec_mode}] Start! ==========')

        for before, after in self.file_conversion_map.items():
            self.__output__(
                f'========== [{self.exec_mode}] Replacing the delimiter: `{before}` => `{after}` =========='
            )
            if self.mode == 'e':
                if re.search(r'Disc\d{1}/', after):
                    os.makedirs(os.path.dirname(after), exist_ok = True)
                if before != after:
                    shutil.move(before, after)

        self.__output__(f'========== [{self.exec_mode}] Done! ==========')
        self.__output__(f'========== [{self.exec_mode}] Total Target File Count: {len(self.paths)} ==========')

    # private

    def __file_conversion_map__(self):
        """Generate a mapping of original paths to new paths with updated delimiters.
        
        Returns:
            dict: A dictionary mapping original file paths to new file paths.
        """
        file_conversion_map = {}
        for path in self.paths:
            file_conversion_map[path] = self.__after__(path)

        return file_conversion_map

    def __after__(self, path):
        """Transform a file path by replacing delimiters according to the pattern.
        
        Returns:
            str: The transformed file path.
        """
        elements     = path.split('/')
        old_filename = elements[-1]

        if re.match(r'^\d-', old_filename):
            new_filename = re.sub(
                r'(?P<disc_number>Disc\d)/(?P<track_number>\d{2})\s',
                rf'\g<disc_number>/\g<track_number>{self.delimiter}',
                re.sub(r'^(?P<disc_number>\d)-', r'Disc\g<disc_number>/', old_filename)
            )
        else:
            new_filename = re.sub(
                r'(?P<track_number>\d{2})\s',
                rf'\g<track_number>{self.delimiter}',
                old_filename
            )

        elements[-1] = new_filename

        return '/'.join(elements)

    def __exec_mode__(self):
        """Determine the execution mode string for output messages.
        
        Returns:
            str: Either 'EXECUTION' or 'DRY RUN'.
        """
        return 'EXECUTION' if self.mode == 'e' else 'DRY RUN'

    def __is_test_env__(self):
        """Check if running in a test environment.
        
        Returns:
            bool: True if in test environment, False otherwise.
        """
        return self.env == 'test'

    def __output__(self, message):
        """Output a message if not running in the test environment.

        Args:
            message: The message to output.

        Returns:
            None
        """
        if not self.__is_test_env__():
            print(message)
