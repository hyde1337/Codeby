get = 15625
i = 1
years = 10
money = 1000000

while get < money:
    get *= 2
    i += 1
else:
    print('Понадобиться {} лет, чтобы стать миллионером при доходе {}$ в год.'.format(i, 15625))

for i in range(9, 0, -1):
    money /= 2
    if i == 1:
        print(f'Понадобиться заработать в первый год{money: .2f}$, чтобы стать миллионером за{years: d} лет.')
