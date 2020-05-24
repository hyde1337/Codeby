# Дано
adress = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print('.'.join([adress[0] + adress[1] + adress[6]] + [adress[9]] + [adress[9]] + [adress[0]]))
# Чистим список от лишнего
del adress[2:6]
del adress[3:5]
# Добавляем недостающие значения
adress.extend('01')
# Составляем финальный адрес в список и делаем из него строку с сепаратороv в виде строки
final_adress = '.'.join([adress[0] + adress[1] + adress[2]] + adress[3:6])
# Вывод
print(final_adress)
