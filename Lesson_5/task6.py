num = int(input('Введите число от 1 до 12: '))
seasons = {0: 'Январь', 1: 'Февраль', 2: 'Март', 3: 'Апрель', 4: 'Май', 5: 'Июнь',
           6: 'Июль', 7: 'Август', 8: 'Сентябрь',  9: 'Октябрь', 10: 'Ноябрь',
           11: 'Декабрь'}

if 1 <= num <= 12:
    if num == 12 or num == 1 or num == 2:
        if num == 12:
            print('Зима,', seasons.get(0))
        elif num == 1:
            print('Зима,', seasons.get(1))
        elif num == 2:
            print('Зима,', seasons.get(2))
    if 3 <= num <= 5:
        if num == 3:
            print('Весна,', seasons.get(3))
        elif num == 4:
            print('Весна,', seasons.get(4))
        elif num == 5:
            print('Весна,', seasons.get(5))
    if 6 <= num <= 8:
        if num == 6:
            print('Лето,', seasons.get(6))
        elif num == 7:
            print('Лето,', seasons.get(7))
        elif num == 8:
            print('Лето,', seasons.get(8))
    if 9 <= num <= 11:
        if num == 9:
            print('Осень,', seasons.get(9))
        elif num == 10:
            print('Осень,', seasons.get(10))
        elif num == 11:
            print('Осень,', seasons.get(11))
else:
    print('Введите число от 1 до 12')