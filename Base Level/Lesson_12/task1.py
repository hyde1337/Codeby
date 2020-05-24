class Valera:
    """Программа считает количество символов без учета пробелов"""
    def __init__(self):
        a = input('Введите предложение: ')
        self.valera_method(a)

    def valera_method(self, b):
        replaced = b.replace(' ', '')
        self.print_results(len(replaced))

    def print_results(self, target_length):
        print('В предложении', target_length, 'символов')


x = Valera()
print(Valera.__doc__)
