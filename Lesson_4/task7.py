xyz = '1', '2', '3', '4'
abc = ('первый', 'второй', 'третий', 'четвертый')

finaDict = dict([(abc[0:1] + xyz[0:1])] + [(abc[1:2] + xyz[1:2])] + [(abc[2:3] + xyz[2:3])] + [(abc[3:4] + xyz[3:4])])
finadict1 = {abc[0]: xyz[0], abc[1]: xyz[1], abc[2]: xyz[2], abc[3]: xyz[3]}

print(tuple(finadict1.keys()))
print(tuple(finaDict.keys()))
