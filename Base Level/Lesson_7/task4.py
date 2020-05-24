def test():
    new = []
    while True:
        args = str(input('Введите любое слово: '))
        if args == '':
            break
        else:
            new.append(args)
    return new


print(test())

