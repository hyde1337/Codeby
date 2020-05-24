class Person:
    def __init__(self, cash, name, position):
        self.__cash = cash
        self.name = name
        self. position = position

    def money(self):
        return self.__cash


people = Person('20000', 'Вася', 'Дворник')
man = Person('150000', 'Жора', 'Гендиректор')


print(people.position, people.name, 'получил зарплату', people.money(), 'рублей')
print(man.position, man.name, 'получил зарплату', man.money(), 'рублей')