# Дано
tool = 'Super-Puper MainTool /v2*'
# Мультиплицируем звездочки
stars = tool[24] * 14
# Выделяем слово 'word'
superWord = tool[0:5]
# Выделяем слово 'tool'
toolWord = tool[16:20]
# Меняем цифру 2 на цифру 1
number = tool[22:24].replace('2', '1')
# Выводим результат
print(stars)
print(' ' + superWord + toolWord, number)
print(stars)
