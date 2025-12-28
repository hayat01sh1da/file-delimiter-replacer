import sys
sys.path.append('./src')

from application import Application

extension = input('Provide the target extension of files whose delimiter you would like to make changes to: ').strip()
delimiter = input('Provide the delimiter to replace spaces with (default `_`): ').strip()
mode      = input('Provide the mode (`d` for dry-run, `e` for execution). Default is `d`: ').strip().lower()

params = dict()
for key, value in { 'extension': extension, 'delimiter': delimiter, 'mode': mode }.items():
    if value:
        params[key] = value

Application(**params).run()
