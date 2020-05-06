import time

print('Время пошло!\n')
t0 = time.time()
textInput = str(input('Введите текст: '))
t1 = time.time()

takenTime = t1 - t0
spm = 60 / (takenTime / len(textInput))
print('Прошло', round(takenTime, 3), 'сек.')
print('Ваша скорость набора', round(spm), 'знаков в минуту')
