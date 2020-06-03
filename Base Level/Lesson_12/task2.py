class Test:
    def __init__(self):
        bullets = int(input('Введите количество патронов: '))
        self.countbullets(bullets)

    def countbullets(self, bullets_shot):
        if 250 <= bullets_shot <= 10000:
            shots = bullets_shot / (1200 / 60)
            changes = bullets_shot // 250
            if bullets_shot == 250:
                changes = 0
            tchanges = changes * 20
            time = shots + tchanges
            self.print_results(time)
            return time
        else:
            print('Введите число от 250 до 10000')

    def print_results(self, kolvo):
        print('Патроны закончатся через', kolvo, 'сек.')


execute_class = Test()
