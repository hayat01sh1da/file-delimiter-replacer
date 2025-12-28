## 1. Environment

- Ruby 4.0.0

## 2. Execution

```command
$ cd ./ruby
$ ruby main.rb 
Provide the target extension of files whose delimiter you would like to make chances to:
.m4a
Provide the delimiter you would like to replace the original one with(Default: `_`):
_
Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!
e
Target extension is .m4a
========== [EXECUTION] Total File Count to Clean: 4 ==========
========== [EXECUTION] The delimiters of those files will be replaced with _ ==========
========== [EXECUTION] Start! ==========
========== [EXECUTION] Replacing the delimiter: ./Artist/Album1/1-01 Title.m4a => ./Artist/Album1/Disc1/01_Title.m4a ==========
========== [EXECUTION] Replacing the delimiter: ./Artist/Album1/2-01 Title.m4a => ./Artist/Album1/Disc2/01_Title.m4a ==========
========== [EXECUTION] Replacing the delimiter: ./Artist/Album2/01 Title.m4a => ./Artist/Album2/01_Title.m4a ==========
========== [EXECUTION] Replacing the delimiter: ./Artist/Album2/02 Title.m4a => ./Artist/Album2/02_Title.m4a ==========
========== [EXECUTION] Done! ==========
========== [EXECUTION] Total Target File Count: 4 ==========
```
