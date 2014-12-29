HeaderCommentChanger
====================

Header comment changer is a Python script to batch change the header comment (usually copyright information) for your .h, .m and .swift files.

## Usage

Use it in Terminal by typing:

'''
> python headercommentchanger.py -d DIR_FOR_THE_FILES_TO_BE_CHANGED -f PATH_OF_THE_NEW_HEADER_FILE_TO_BE_ADDED_TO_THE_FILES

'''

If you do not specify `DIR_FOR_THE_FILES_TO_BE_CHANGED` or `PATH_OF_THE_NEW_HEADER_FILE_TO_BE_ADDED_TO_THE_FILES`, the default values are:
`DIR_FOR_THE_FILES_TO_BE_CHANGED`: the same directory as `headercommentchanger.py`
`PATH_OF_THE_NEW_HEADER_FILE_TO_BE_ADDED_TO_THE_FILES`: `newheader.txt` in `headercommentchanger.py`'s directory

Help information:

'''
usage: headercommentchanger.py [-h] [-d DIR] [-f NEWHEADERFILE]

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --dir DIR     directory of the files to be changed
  -f NEWHEADERFILE, --newheaderfile NEWHEADERFILE
                        path of the new header file to be added to the files
                        in the directory

'''

## Example

I would like to change all .h, .m and .swift files in `/Repos/YZLibrary/YZLibraryDemo/YZLibraryDemo` by adding the content of `/Repos/HeaderCommentChanger/newheader.txt`

I would be running this command:

'''
> python headercommentchanger.py -d /Repos/YZLibrary/YZLibraryDemo/YZLibraryDemo -f /Repos/HeaderCommentChanger/newheader.txt 

'''

The content of `/Repos/HeaderCommentChanger/newheader.txt`:
![Content of new header](https://github.com/yichizhang/HeaderCommentChanger/blob/master/Screenshots/screenshot_newheader.png)

### Before
![File 1 Before](https://github.com/yichizhang/HeaderCommentChanger/blob/master/Screenshots/screenshot_file1_before.png)
![File 2 Before](https://github.com/yichizhang/HeaderCommentChanger/blob/master/Screenshots/screenshot_file2_before.png)

### After
![File 1 After](https://github.com/yichizhang/HeaderCommentChanger/blob/master/Screenshots/screenshot_file1_after.png)
![File 1 Git](https://github.com/yichizhang/HeaderCommentChanger/blob/master/Screenshots/screenshot_file1_git.png)
![File 2 After](https://github.com/yichizhang/HeaderCommentChanger/blob/master/Screenshots/screenshot_file2_after.png)
![File 2 Git](https://github.com/yichizhang/HeaderCommentChanger/blob/master/Screenshots/screenshot_file2_git.png)
