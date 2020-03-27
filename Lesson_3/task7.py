# Дано
slice_string = ['pgekjsgqlafrimzixwuiavukxdqifadmbdqvszcqizimkifcajycqijwuwwawmbbiiigevfrualbsgijbvskfskwczlbervxkmsgtxr'
                'fxswmxsibffvaqrabgwxwcqzcrjiedsizjauufrfdiguzjxhcwlgjiduemddufkewasjfgavsrujgbisagzswdaeebwerdcluoqvgaj'
                'abbelaadswzdebwgxvdfaugqjazlwvzejdgleszsrlqxnsrkbkqcvgwekwsqezll']
# Переведем список с одним элементом в строку, затем сделаем из этой строки новый список по элементу и будем работать
# с новым списком
i = ''.join(slice_string)
b = list(i)
# На данном этапе почекав индексы командой c = b.index('*'), увидел, что каждая нужная буква занимает значение индекса
# с шагом в 50, значит можно использовать один слайс и сразу сделать нужное слово, а затем просто перевести в строку
g = b[::50]
# Выводим результат в виде строки, используя метод join
print(''.join(g))
