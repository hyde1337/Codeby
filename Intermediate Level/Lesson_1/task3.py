import argparse


class ValueExtract:
    def __init__(self):
        self.value = args.value.lower()
        self.file_read()

    def file_read(self):
        with open('phonebook_al.txt', 'r', encoding='utf8') as file:
            content = file.readlines()
        self.ext_and_condition(content, self.value)

    @staticmethod
    def ext_and_condition(content, value):
        list_for_len = []
        for i in content:
            lowercase = [i.lower() for i in i.split()]
            for_print = [i.capitalize() for i in lowercase]
            if value in lowercase:
                if '@' in i:
                    print(' '.join(for_print[:-1]))
                    list_for_len.append(i)
                else:
                    print(' '.join(for_print))
                    list_for_len.append(i)
        print('Найдено', len(list_for_len), 'записи(ей)')


parser = argparse.ArgumentParser(description='Выделяет заданное значение и выводит строку с ним в консоль')
parser.add_argument('value', type=str)
args = parser.parse_args()

ValueExtract()
