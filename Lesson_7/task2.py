bullets = int(input('Введите количество патронов: '))


def countbullets(args):
    if 250 <= args <= 10000:
        shots = args / (1200 / 60)
        changes = args // 250
        if args == 250:
            changes = 0
        tchanges = changes * 20
        time = shots + tchanges
        return time
    else:
        print('Введите число от 250 до 10000')


print('Патроны закончатся через', countbullets(bullets), 'сек.')
