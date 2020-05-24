import animals
import random

d = {1: animals.deer, 2: animals.cat, 3: animals.cow, 4: animals.frog, 5: animals.bat, 6: animals.butterfly,
     7: random.randrange(1, 7)}
print("""Help:

    1) deer
    2) cat
    3) cow
    4) frog
    5) bat
    6) butterfly
    7) random
""")
try:
    number = int(input('Введите номер рисунка: '))
except ValueError:
    print('Введите число!')
except NameError:
    print('Введите число!')
except KeyboardInterrupt:
    print('\nПрервано пользователем!')

else:
    if number in d:
        if number == 7:
            number = d.get(number)
        print(d.get(number))
    else:
        print('Введите число от 1 до 7')
