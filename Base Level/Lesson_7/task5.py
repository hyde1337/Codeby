chisla = input('Ввести числа: ').split()


def area(*params):
    my_list = params[0]
    if len(my_list) == 0:
        print('Заданных параметров для вычисления не найдено!')
    if len(my_list) == 1:
        print('Площадь круга:', int(my_list[0]) * int(my_list[0]), 'кв. метров')
    if len(my_list) == 2:
        print('Площадь прямоугльника:', int(my_list[0]) * int(my_list[1]), 'кв. метров')
    if len(my_list) == 3:
        if int(my_list[0]) == int(my_list[1]) == int(my_list[2]):
            p = int(my_list[0]) + int(my_list[1]) + int(my_list[2])
            s = (p * (p - int(my_list[0])) * (p - int(my_list[1])) * (p - int(my_list[2]))) ** 0.5
        else:
            p = 0.5 * (int(my_list[0])) + int(my_list[1]) + int(my_list[2])
            s = (p * (p - int(my_list[0])) * (p - int(my_list[1])) * (p - int(my_list[2]))) ** 0.5
        print('Площадь прямоугльника:', round(s), 'кв. метров')


area(chisla)

