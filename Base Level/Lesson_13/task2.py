class Avans:
    def __init__(self, name, prepayment, summa):
        self.name = name
        self.prepayment = prepayment
        self.summa = summa


class Zarplata(Avans):
    def __init__(self, salary, summa2):
        self.salary = salary
        self.summa2 = summa2
        super().__init__(name='Александр Курицын', prepayment=25000, summa=0)


avans = Avans('Александр Невский', 10000, 20000)
zarplata = Zarplata(10000, 0)

print('{} - аванс {} рублей'.format(avans.name, avans.prepayment))
print('{} - аванс {} рублей, зарплата {} рублей'.format(zarplata.name, zarplata.prepayment,
                                                        str(zarplata.salary + zarplata.prepayment)))
