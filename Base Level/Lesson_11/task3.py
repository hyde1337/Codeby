with open('symbol.txt', 'r', encoding='utf8') as file:
    content = file.readline()
    length = int(len(content) / 8)
    c = 0
    d = 8
    for i in range(0, length):
        print('{}{}{}'.format(8 * ',', content[c:d], 8 * '.'))
        c += 8
        d += 8
