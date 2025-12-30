## 1. Common Environment

- WSL(Ubuntu 24.4.3 LTS)

## 2. READMEs

- [Ruby](./ruby/README.md)
- [Python](./python/README.md)

## 3. Source Codes

- [Ruby](./ruby/)
- [Python](./python/)

## 4. How to Use

iTUnes provides no user interface to control the delimiter when importing songs from CDs.  
The format of filepath is `Artist/Album/1-01 Title.m4a`, for example.  
`\d{1}\-` prefix represents the disc number.  
The script aims to convert the path as follows, for example.

|Before |After |
|:-|:-|
|Artist/Album/1-01 Title.m4a |Artist/Album/Disc/01_Title.m4a |

It requires use to input the following 3 parameters to replace the original delimiter with something else you prefer.

- `extension`: The target extension of files whose delimiter you would like to make changes to
- `delimiter`: The delimiter you would like to replace the original one with
- `mode`: The operation is done as the execution mode with `e` and the dry_run mode without any option
