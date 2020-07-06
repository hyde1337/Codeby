# import re
#
# with open('job.txt', 'r', encoding='utf8') as file:
#     for line in file:
#         content = file.readline()
#         res = re.search(r'[К-С]\w{5}[к]', content)
#         if res:
#             print(res.group())
#

import re

with open('job.txt', 'r', encoding='utf8') as file:
    content = ' '.join(file.readlines())
    res = re.findall(r'[К-С]\w{5}[к]', content)
    if res:
        print('\n'.join(res))




