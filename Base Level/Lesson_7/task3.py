word = input('Введите слово: ')
comparison = lambda x: 'Это слово больше, чем predator' if word > 'predator' else 'Это слово меньше, чем predator'
print(comparison(word))
