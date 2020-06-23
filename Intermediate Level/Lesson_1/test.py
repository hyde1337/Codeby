def file_read(self):
    with open('phonebook_al.txt', 'r', encoding='utf8') as file:
        content = file.readlines()
    self.ext_and_condition(content, self.value)


with open('phonebook_al.txt', 'r', encoding='utf8') as file:
    content = file.readlines()
self.ext_and_condition(content, self.value)

