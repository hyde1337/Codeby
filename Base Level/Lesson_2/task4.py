# Дано
city = 'города - масква, лондон, париж, берлин...'
# Выведем результат
print(city.title().replace(' - ', ': ').replace('а', 'о', 2).replace('о', 'а', 3).replace('а', 'о', 2).replace('...',
                                                                                                               '.'))
