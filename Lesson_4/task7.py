xyz = '1', '2', '3', '4'
abc = ('первый', 'второй', 'третий', 'четвертый')

finaDict = dict([(abc[0:1] + xyz[0:1])] + [(abc[1:2] + xyz[1:2])] + [(abc[2:3] + xyz[2:3])] + [(abc[3:4] + xyz[3:4])])

print(tuple(finaDict.keys()))
