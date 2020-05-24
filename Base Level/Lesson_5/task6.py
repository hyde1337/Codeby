num = int(input('Введите число от 1 до 12: '))
seasons = {0: 'Январь', 1: 'Февраль', 2: 'Март', 3: 'Апрель', 4: 'Май', 5: 'Июнь',
           6: 'Июль', 7: 'Август', 8: 'Сентябрь',  9: 'Октябрь', 10: 'Ноябрь',
           11: 'Декабрь'}
if 1 <= num <= 12:
    if num in (12, 1, 2):
        print('Зима,', seasons.get(num - 1))
    elif 3 <= num <= 5:
        print('Весна,', seasons.get(num - 1))
    elif 6 <= num <= 8:
        print('Лето,', seasons.get(num - 1))
    elif 9 <= num <= 11:
        print('Осень,', seasons.get(num - 1))
else:
    print('Введите число от 1 до 12!')
