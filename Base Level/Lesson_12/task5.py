class Trap:
    def __init__(self):
        d1 = int(input('Введите диагональ трапеции 1: '))
        d2 = int(input('Введите диагональ трапеции 2: '))
        h = int(input('Введите высоту трапеции 1: '))
        if d1 > h and d2 > h:
            self.space(d1, d2, h)
        else:
            print('Введите корректные параметры трапеции.')

    def space(self, dia1, dia2, hv):
        s = (((((dia2**2) - (hv**2))**0.5) + (((dia1**2) - (hv**2))**0.5)) / 2) * hv
        print('Площадь трапеции: {:.2f} кв.м'.format(s))


Trap()
