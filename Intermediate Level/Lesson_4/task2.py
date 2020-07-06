import re

with open('proxy.txt', 'r', encoding='utf8') as file:
    for line in file:
        content = file.readline()
        res = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', content)
        print(res.group())
