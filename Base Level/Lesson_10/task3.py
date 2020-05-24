with open('city.txt', 'r', encoding='utf8') as file:
    content = file.readlines()

with open('city_o.txt', 'w', encoding='utf8') as file_o:
    for i in content:
        if 'о' not in i:
            file_o.write(i)
