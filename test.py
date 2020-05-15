import random

rnumber = random.randint(1, 10)

i = 0
while i < 3:
    try:
        unumber = int(input('Введите число от 1 до 10: '))
    except KeyboardInterrupt:
        print('\nПрервано пользователем!')
    except ValueError:
        print('Введите число!')
    else:
        i += 1
        if i == 3:
            print('Удача не на твоей стороне, попробуй ещё!')
            break
        elif unumber < 1 or unumber > 10:
            print('Ошибка! Введите число от 1 до 10!')
        elif unumber > rnumber:
            print('Ваше число больше!')
        elif unumber < rnumber:
            print('Ваше число меньше!')
        else:
            print('Вы победили!')
            break
