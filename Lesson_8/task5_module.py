def textch(arg):
    middle = '|'.join(arg)
    print('+-' * len(arg) + '+')
    print('|' + middle + '|')
    print('+-' * len(arg) + '+')


m = input('Введите текст: ')
textch(m)
