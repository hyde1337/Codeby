i = 1
with open('numbers.txt', 'w', encoding='utf8') as file:
    for i in range(1, 10001):
        file.write((str(i)) + '\n')
        i += 1
