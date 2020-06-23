import os
import argparse
import stat


class Commands:
    def __init__(self):
        self.value = args.value
        self.chmod = args.chmod
        self.tree = args.tree
        if self.value == 'system':
            self.system_commands(self.value)
        if self.chmod == 'chmod':
            self.chmod_path(self.chmod)
        if self.tree == 'tree':
            self.tree_path(self.tree)

    @staticmethod
    def system_commands(value):
        while value:
            command = str(input('Shell Command: '))
            if command == 'exit':
                print('The work was completed!')
                break
            if command != '0':
                print('Wrong Command, exit!')
                break
            print(str(os.system(command))[10:])

    @staticmethod
    def chmod_path(chmod):
        while chmod:
            command = str(input('Enter the path: '))
            if command == 'exit':
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
            for root, dirs, files in os.walk(command):
                level = root.replace(command, '').count(os.sep)
                indent = ' ' * 5 * level
                subindent = ' ' * 4 * (level + 1)
                print('{}|-{}'.format(indent, os.path.basename(root)))
                for f in files:
                    print('|{}|-{}'.format(subindent, f))


parser = argparse.ArgumentParser(description='Выделяет заданное значение и выводит строку с ним в консоль')
parser.add_argument('-s', '--value', type=str, help='System Command')
parser.add_argument('-c', '--chmod', type=str, help='Checking Access Rights')
parser.add_argument('-t', '--tree', type=str, help='Directory Tree')
args = parser.parse_args()


Commands()
