import random
import time

one = random.randint(10, 30) * '#'
two = random.randint(10, 30) * '#'
three = random.randint(10, 30) * '#'

print('1)')
for i in one:
    print('#', end='')
    time.sleep(0.5)

print('\n2)')
for i in two:
    print('#', end='')
    time.sleep(0.5)

print('\n3)')
for i in three:
    print('#', end='')
    time.sleep(0.5)

if len(one) > len(two) and len(one) > len(three):
    print('\nДорожка one из ', len(one), 'сим. победила!')
elif len(two) > len(one) and len(two) > len(three):
    print('\nДорожка two из ', len(two), 'сим. победила!')
elif len(three) > len(one) and len(three) > len(two):
    print('\nДорожка three из ', len(three), 'сим. победила!')
