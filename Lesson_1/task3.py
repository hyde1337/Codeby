# Для подсчета площади дома Юрия, можно использовать формулу площади прямоугольника a * b
ura_house = 7 * 9
# Для подсчета площади дома Александра, можно использовать формулу площади круга S = pir^2, возьмем pi = 3.14
alex_house = 3.14 * ((9 / 2) ** 2)
# Дом Владимира с выемкой, значит, чтоб найти площадить его дома, необходимо вычесть из общей площади, площадь выемки
vladimir_house = (8 * 9) - (3 * 2)
# Выведем результат проверки размеров домов через оператор and
print('Проверим, Дом Юры меньше домов Александра и Владмимира:', ura_house < alex_house and ura_house < vladimir_house)
print('Проверим, Дом Алексадра меньше домов Владимира и Юрия:', alex_house < vladimir_house and alex_house < ura_house)
print('Проверим, Дом Владимира меньше домов Александра и Юрия:', vladimir_house < alex_house and
      vladimir_house < ura_house)

print(ura_house)
print(alex_house)
print(vladimir_house)

