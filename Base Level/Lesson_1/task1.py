# Зададим переменные по количеству ботов
all_bots = 1000
lose_bots = 2
added_or_not_bots = 3
days = 30
# Зададим формулы на вычисление
result_add = all_bots - (lose_bots * days) + (added_or_not_bots * days)
result_not_add = all_bots - lose_bots * days
# Выведем результаты вычислений
print('Если добавлять по 3 бота:', result_add)
print('Если не добавлять по 3 бота:', result_not_add)
