import os
import argparse
import stat


class Commands:
    def system_commands(self):
        while (command := input('Shell Command: ')) != 'exit':
            if str(os.system(command))[0] != '0':
                print('Wrong Command, exit!')
                break
        else:
            print('The work was completed!')

    def chmod_path(self):
        while (command := input('Enter the path: ')) != 'exit':
            if os.path.exists(command) is True :
                print(str(oct(stat.S_IMODE(os.lstat(command).st_mode)))[2:])
            else:
                print('The file or directory does not exist!')
        else:
            print("The work was completed!")

    def tree_path(self):
        while (command := input('Enter the path: ')) != 'exit':
            if os.path.exists(command) is True:
                print(str(os.system('tree -n ' + command))[10:])
                os.system('tree -n ' + command + ' >> test{}'.format('wood_' + command.split('/')[-1]))
            else:
                print('The path or directory doesnt exist!')
        else:
            print('The work was completed!')


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--value', type=str, help='System Command')
parser.add_argument('-c', '--chmod', type=str, help='Checking Access Rights')
parser.add_argument('-t', '--tree', type=str, help='Directory Tree')
args = parser.parse_args()

tmp = Commands()

if args.chmod == 'chmod':
    tmp.chmod_path()
elif args.tree == 'tree':
    tmp.tree_path()
elif args.value == 'system':
    tmp.system_commands()
else:
    parser.print_help()
