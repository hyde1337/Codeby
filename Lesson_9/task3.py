import time
try:
    number = int(input('Введите число от 10 до 30: '))
except ValueError:
    print('Введите число!')
except NameError:
    print('Введите число!')
except KeyboardInterrupt:
    print('\nПрервано пользователем!')

else:
    if 10 <= number <= 30:
        for i in range(number, -1, -1):
            print(i, end='')
            time.sleep(1)
            print('\r', end='')
            if i == 0:
                break
    else:
        print('Введите число от 10 до 30!')
