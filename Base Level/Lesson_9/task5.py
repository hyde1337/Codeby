import string


def is_length_valid(arg):
    if 8 <= len(arg) <= 20:
        return True


def is_frst_lstsymbs_valid(arg):
    if arg[0] in string.ascii_uppercase and arg[-1] in string.hexdigits:
        return True


def is__in(arg):
    if '_' in arg:
        return True


def is_all_symbs_valid(arg):
    for i in arg:
        if i in string.hexdigits:
            return True


try:
    password = str(input('Введите пароль: '))
except KeyboardInterrupt:
    print('\nПрервано пользователем!')
else:
    if is_length_valid(password) and is_frst_lstsymbs_valid(password) and is__in(password) and is_all_symbs_valid\
                (password):
        print('Пароль принят!')
    else:
        print('Пароль не соответствует требованиям!')
