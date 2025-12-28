## 1. Environment

- Python 3.14.2

## 2. Execution

```command
$ cd ./python
$ python test/test_application_.py 
....
----------------------------------------------------------------------
Ran 4 tests in 0.601s

OK
hayat01sh1da@HAYAT01SH1DA:/mnt/c/Users/binlh/Documents/development/file-delimiter-replacer/python$ python main.py
Provide the target extension of files whose delimiter you would like to make changes to: .m4a
Provide the delimiter to replace spaces with (default `_`): _
Provide the mode (`d` for dry-run, `e` for execution). Default is `d`: e
Target extension is `.m4a`
========== [EXECUTION] Total File Count to Clean: 4 ==========
========== [EXECUTION] The delimiters of those files will be replaced with `_` ==========
========== [EXECUTION] Start! ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album1/Disc1/01_Title.m4a` => `./Artist/Album1/Disc1/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album1/Disc2/01_Title.m4a` => `./Artist/Album1/Disc2/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album2/01_Title.m4a` => `./Artist/Album2/01_Title.m4a` ==========
========== [EXECUTION] Replacing the delimiter: `./Artist/Album2/02_Title.m4a` => `./Artist/Album2/02_Title.m4a` ==========
========== [EXECUTION] Done! ==========
========== [EXECUTION] Total Target File Count: 4 ==========
```
