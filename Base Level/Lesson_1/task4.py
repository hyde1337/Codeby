# Рассчитаем общее расстояние, которое необходимо преодолеть пешеходу, необходми перевести в единую систему счисления
distance = ((60 * 10) * 30) / 1000
# После того, как посчитали общее расстояние, разделим на скорость движения пешехода
peshehod_time = ((distance / 4) - 2)
# Выведем время движения
print('Пешеходу осталось идти', peshehod_time, 'часа.')
