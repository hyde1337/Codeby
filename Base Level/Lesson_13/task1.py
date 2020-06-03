class Films:
    def __init__(self, title, name, surname):
        self.title = title
        self.name = name
        self.surname = surname


class FilmsRu(Films):
    def __init__(self, title, name, surname):
        super().__init__(title, name, surname)


def print_films(arg):
    for num in range(0, 5):
        print('{} - в главной роли {} {}'.format(arg[num].title, arg[num].name, arg[num].surname))


first_film = Films('Человек-Паук', 'Тоби', 'Магуайэр')
second_film = Films('Список Шиндлера', 'Лиам', 'Нисон')
third_film = Films('Мстители', 'Роберт', 'Дауни Младший')
fourth_film = Films('Джентельмены', 'Мэтью', 'Макконахи')
fifth_film = Films('Враг', 'Джейк', 'Джилленхол')

first_film_ru = FilmsRu('Притяжение', 'Александр', 'Петров')
second_film_ru = FilmsRu('Максимальный удар', 'Алесандр', 'Невский')
third_film_ru = FilmsRu('Идеальный мужчина', 'Егор', 'Крид')
fourth_film_ru = FilmsRu('На Районе', 'Данила', 'Козловский')
fifth_film_ru = FilmsRu('Дед Мороз', 'Фёдор', 'Бондарчук')

films_eu = [first_film, second_film, third_film, fourth_film, fifth_film]
films_ru = [first_film_ru, second_film_ru, third_film_ru, fourth_film_ru, fifth_film_ru]

print_films(films_eu)
print()
print_films(films_ru)
