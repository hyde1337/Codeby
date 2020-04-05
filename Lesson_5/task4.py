num1 = str(input('Введите строку: '))
if 0 <= len(num1) <= 100:
    if 5 <= len(num1) <= 100 or len(num1) == 0:
        print('В строке', len(num1), 'символов')
    elif 2 <= len(num1) <= 4:
        print('В строке', len(num1), 'символа')
    elif len(num1) == 1:
        print('В строке', len(num1), 'символ')
else:
    print('Количество символов не должно быть больше 100!')
