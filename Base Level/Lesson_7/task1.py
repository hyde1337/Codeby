a = input('Введите предложение: ')


def count_spaces(b):
    """Программа считает количество символов без учета пробелов"""
    replaced = b.replace(' ', '')
    return len(replaced)


print('В предложении', count_spaces(a), 'символов')
print(count_spaces.__doc__)
