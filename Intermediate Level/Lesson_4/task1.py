import re


text = 'Московское время 10:36:06'
res = re.search(r'([01]\d|2[0-3]):([0-5]\d):([0-5]\d)', text)
print(res.group())
