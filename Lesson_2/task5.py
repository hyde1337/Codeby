# Дано
history = 'История Python, одного из самых простых языков программирования, началась в 1989 году.'  # "простор"
# Выводим результаты разными способами
print(history[32:37] + history[3:5])
#####################################
chHistory = history[32:39]
print(chHistory.replace('ых', 'ор'))
#####################################
print(history[47:50] + history[1:5])
#####################################
fromPython = history[8].lower()
fromLast = history[4] + history[3] + history[2] + history[1] + history[12] + fromPython + history[47]
print(fromLast[::-1])
