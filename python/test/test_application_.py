import glob
import os
import shutil
import sys
import unittest

sys.path.append('./src')

from application import Application, InvalidModeError

class TestApplication(unittest.TestCase):
    def setUp(self):
            self.extension = '.m4a'
            self.base_dir  = os.path.join('.', 'test', 'Artist')
            self.pycaches  = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
            paths          = (
                os.path.join(self.base_dir, 'Album1', f'1-01 Title{self.extension}'),
                os.path.join(self.base_dir, 'Album1', f'2-01 Title{self.extension}'),
                os.path.join(self.base_dir, 'Album2', f'01 Title{self.extension}'),
                os.path.join(self.base_dir, 'Album2', f'02 Title{self.extension}'),
                os.path.join(self.base_dir, 'Album3', '01 Title.mp3')
            )

            for path in paths:
                directory = os.path.dirname(path)
                os.makedirs(directory, exist_ok=True)
                with open(path, 'w', encoding='utf-8') as file_handle:
                   file_handle.write('')

    def tearDown(self):
            if os.path.exists(self.base_dir):
                shutil.rmtree(self.base_dir)
            for pycache in self.pycaches:
                if os.path.exists(pycache):
                    shutil.rmtree(pycache)

    def test_invalid_mode(self):
        with self.assertRaises(InvalidModeError) as cm:
            Application(extension = self.extension, mode = 'a').run()
        self.assertEqual('a is invalid mode. Provide either `d`(default) or `e`.', str(cm.exception))

    def test_dry_run_keeps_original_files(self):
        Application(extension = self.extension).run()

        self.assertEqual(
            [
                './test/Artist/Album1/1-01 Title.m4a',
                './test/Artist/Album1/2-01 Title.m4a',
                './test/Artist/Album2/01 Title.m4a',
                './test/Artist/Album2/02 Title.m4a',
                './test/Artist/Album3/01 Title.mp3'
            ],
            sorted(glob.glob(os.path.join(self.base_dir, '**', '*.*'), recursive=True))
        )

    def test_execution_mode_restructures_files(self):
        Application(extension = self.extension, mode = 'e').run()

        self.assertEqual(
            [
                './test/Artist/Album1/Disc1/01_Title.m4a',
                './test/Artist/Album1/Disc2/01_Title.m4a',
                './test/Artist/Album2/01_Title.m4a',
                './test/Artist/Album2/02_Title.m4a',
                './test/Artist/Album3/01 Title.mp3'
            ],
            sorted(glob.glob(os.path.join(self.base_dir, '**', '*.*'), recursive=True))
        )

    def test_execution_mode_with_custom_delimiter(self):
        Application(extension = self.extension, delimiter = '-', mode = 'e').run()

        self.assertEqual(
            [
                './test/Artist/Album1/Disc1/01-Title.m4a',
                './test/Artist/Album1/Disc2/01-Title.m4a',
                './test/Artist/Album2/01-Title.m4a',
                './test/Artist/Album2/02-Title.m4a',
                './test/Artist/Album3/01 Title.mp3'
            ],
            sorted(glob.glob(os.path.join(self.base_dir, '**', '*.*'), recursive=True))
        )

if __name__ == '__main__':
   unittest.main()
