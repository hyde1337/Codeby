import os
import argparse
import stat
import sys


class Commands:
    def __init__(self):
        self.value = args.value
        self.chmod = args.chmod
        self.tree = args.tree
        if self.value == 'system':
            self.system_commands(self.value)
        else:
            self.fast_commands(self.value)
        if self.chmod == 'chmod':
            self.chmod_path(self.chmod)
        if self.tree == 'tree':
            self.tree_path(self.tree)
        if len(sys.argv) == 1:
            os.system('python task3.py --help')

    @staticmethod
    def system_commands(value):
        while value:
            if (command := str(input('Shell Command: '))) == 'exit':
                print('The work was completed!')
                break
            if str(os.system(command))[0] != '0':
                print('Wrong Command, exit!')
                break

    @staticmethod
    def fast_commands(value):
        while value:
            if value == 'exit':
                print('The work was completed!')
                break
            elif str(os.system(value))[0] != '0':
                print('Wrong Command, exit!')
                break

    @staticmethod
    def chmod_path(chmod):
        while chmod:
            if (command := str(input('Enter the path: '))) == 'exit':
                print('The work was completed!')
                break
            try:
                print(str(oct(stat.S_IMODE(os.lstat(command).st_mode)))[2:])
            except FileNotFoundError:
                print('The file or directory does not exist!')

    @staticmethod
    def tree_path(tree):
        while tree:
            command = str(input('Enter the path: '))
            if command == 'exit':
                print('The work was completed!')
                break
            if os.path.exists(command) is True:
                print(str(os.system('tree -n ' + command))[10:])
                print(str(os.system('tree -n ' + command + '>> test{}'.format('wood_' + command.split('/')[-1])))[10:])
            else:
                print('The path or directory doesnt exist!')


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--value', type=str, help='System Command')
parser.add_argument('-c', '--chmod', type=str, help='Checking Access Rights')
parser.add_argument('-t', '--tree', type=str, help='Directory Tree')
args = parser.parse_args()


Commands()
