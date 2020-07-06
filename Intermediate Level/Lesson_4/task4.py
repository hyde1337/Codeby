import re
try:
    while password := input('Введите пароль:'):
        res = re.match(r'^[A-Z](?=.*[_])(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?!.*\s).{8,16}[a-zA-Z0-9]$', password)
        if res:
            print('Пароль подходит!')
        else:
            print('Пароль не подходит!')
            break
except KeyboardInterrupt:
    print('\nПрервано пользователем!')
