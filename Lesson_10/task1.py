i = 1
with open('numbers.txt', 'w') as file:
    for i in range(1, 10001):
        print(i)
        file.write((str(i)) + '\n')
        i += 1
