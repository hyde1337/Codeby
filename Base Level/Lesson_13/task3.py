class SEllips:
    @staticmethod
    def s():
        try:
            poluos1 = int(input('Введите полуось 1: '))
            poluos2 = int(input('Введите полуось 2: '))
        except ValueError:
            print('Введите число!')
        except NameError:
            print('Введите число!')
        except KeyboardInterrupt:
            print('\nПрервано пользователем!')
        else:
            if poluos1 <= 0 or poluos2 <= 0:
                print('Введите положительные значения!')
            else:
                print('Площадь эллипса: {}'.format(poluos1 * poluos2 * 3.14))


class VKon:
    @staticmethod
    def s():
        try:
            visota = int(input('Введите высоту: '))
            radius = int(input('Введите радиус: '))
        except ValueError:
            print('Введите число!')
        except NameError:
            print('Введите число!')
        except KeyboardInterrupt:
            print('\nПрервано пользователем!')
        else:
            if visota <= 0 or radius <= 0:
                print('Введите положительные значения!')
            else:
                print('Объем конуса: {:.2f}'.format((visota / 3) * 3.14 * radius))


SEllips.s()
VKon.s()
