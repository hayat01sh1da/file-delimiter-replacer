import sys
import os
import shutil
import glob
sys.path.append('./src')
from application import Application

from application import Application

extension = input('Provide the target extension of files whose delimiter you would like to make changes to: ').strip().strip()
delimiter = input('Provide the delimiter to replace spaces with (default `_`): ').strip().strip()
mode      = input('Provide the mode (`d` for dry-run, `e` for execution). Default is `d`: ').strip().lower().strip()

params = dict()
for key, value in { 'extension': extension, 'delimiter': delimiter, 'mode': mode }.items():
    if value:
        params[key] = value

Application(**params).run()

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
