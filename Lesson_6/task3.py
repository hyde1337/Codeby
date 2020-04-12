count = count1 = 0
jewel = ['золото', 'алмазы', 'серебро', 'сапфиры', 'бронза', 'рубины', 'платина', 'изумруды', 'палладий', 'аметисты']
for i in jewel[0::2]:
    count += 1
    print(count, i)
print()
for i in jewel[1::2]:
    count1 += 1
    print(count1, i)
