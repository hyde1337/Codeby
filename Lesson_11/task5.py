import random
from colorama import Fore

dima, vova = random.randint(2, 13), random.randint(2, 13)

while dima == vova:
    print('Игрок Вова набрал {:02d} очк.'.format(vova))
    print('Игрок Дима набрал {:02d} очк.'.format(dima))
    print('Очки у обоих игроков совпали, перебрасываем кости.\n')
    dima, vova = random.randint(2, 13), random.randint(2, 13)
else:
    if vova > dima:
        print('Игрок Вова набрал {:02d} очк.'.format(vova), Fore.GREEN + "You winner" + Fore.RESET)
        print('Игрок Дима набрал {:02d} очк.'.format(dima))
    elif dima > vova:
        print('Игрок Дима набрал {:02d} очк.'.format(dima), Fore.GREEN + "You winner" + Fore.RESET)
        print('Игрок Вова набрал {:02d} очк.'.format(vova))