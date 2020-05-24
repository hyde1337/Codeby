class Colorful:
    """1) Зеленый
2) Красный
3) Синий
4) Пурпурный"""
    def __init__(self):
        color_number = int(input('Выберите цвет: '))
        color_string = str(input('Введите строку: '))
        self.green = '\033[42m' + color_string + '\033[49m'
        self.red = '\033[41m' + color_string + '\033[49m'
        self.blue = '\033[44m' + color_string + '\033[49m'
        self.purple = '\033[45m' + color_string + '\033[49m'
        self.color(color_number)

    def color(self, number):
        if number == 1:
            print(self.green)
        elif number == 2:
            print(self.red)
        elif number == 3:
            print(self.blue)
        elif number == 4:
            print(self.purple)
        else:
            print('Введите число от 1 до 4')


print(Colorful.__doc__)
Colorful()
