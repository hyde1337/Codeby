spaces = 0
for i in range(19, 3, -1):
    if i % 2 == 0:
        spaces += 1
        print(' ' * spaces, '$' * i)
for b in range(4, 19):
    if b % 2 == 0:
        if spaces <= 8:
            spaces -= 1
            print(' ' * spaces + ' ', '$' * b)
