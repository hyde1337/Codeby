def symbols(arg):
    print('В предложении', len(arg), 'символов(л, а)')


def words(arg):
    my_list = arg.split(' ')
    print('В предложении', len(my_list), 'слов(а)')


def countsymb(arg):
    sorted_list = sorted(arg)
    csymbols = {}
    for i in sorted_list:
        if i in csymbols:
            csymbols[i] += 1
        else:
            csymbols[i] = 1
    print("Сколько раз встречается каждый знак:\n" + str(csymbols).replace(', ', '\n').replace('\'', '').
          replace(':', ' -')[1:-1])


if __name__ == '__main__':
    sent = input('Введите предлодение: ')
    symbols(sent)
    words(sent)
    countsymb(sent)
