import os
import stat


def show_cur_rights():
    rights = ['---', '--x', '-w-', 'r-x', 'r--', 'r-x', 'rw-', 'rwx']
    rights_value = oct(stat.S_IMODE(os.lstat(os.getcwd()).st_mode))[2:]
    print('Права текущей директории:')
    for i in rights_value:
        print(rights[int(i)], end='')


show_cur_rights()
