hour = int(input('Введите часы: '))
minute = int(input('Введите минуты: '))
second = int(input('Введите секунды: '))
if hour <= 23 and minute < 60 and second < 60:
    if 0 <= hour <= 9:
        hour = '0' + str(hour)
    if 0 <= minute <= 9:
        minute = '0' + str(minute)
    if 0 <= second <= 9:
        second = '0' + str(second)
        print(hour, minute, second, sep=':')
    else:
        print(hour, minute, second, sep=':')
else:
    print('Введите числа для часов от 0 до 23, и для минут и секунд от 0 до 59')