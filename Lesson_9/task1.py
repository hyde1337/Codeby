import random

try:
    number = int(input('Введите число: '))
except ValueError:
    print('Введите число!')
except NameError:
    print('Введите число!')
except KeyboardInterrupt:
    print('\nПрервано пользователем!')
else:
    if 1 <= number <= 10:
        number2 = random.randint(10, 100)
        print(sum(range(number, number2)))
    else:
        print('Введите число от 1 до 10')
