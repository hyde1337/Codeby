num1 = str(input('Введите строку: '))
if 0 <= len(num1) <= 100:
    if 11 <= len(num1) <= 19:
        print('В строке', len(num1), 'символов')
    else:
        if len(num1) % 10 == 1:
            print('В строке', len(num1), 'символ')
        elif len(num1) % 10 in (2, 3, 4):
            print('В строке', len(num1), 'символа')
        else:
            print('В строке', len(num1), 'символов')
else:
    print('Количество символов не должно быть больше 100!')
