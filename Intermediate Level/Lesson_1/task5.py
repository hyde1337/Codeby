import itertools
import click
import random
import time


@click.command()
@click.argument('number', type=int)
class CombosGenerator:
    def __init__(self, number):
        self.number = number
        self.gen_combos(self.number)

    def gen_combos(self, number):
        start_time = time.time()
        list_of_combs = list(itertools.product('string.digits', repeat=number))
        random.shuffle(list_of_combs)
        for_write = [''.join(i) for i in list_of_combs]
        print('Start process\n' + 'Количество комбинаций:', len(list_of_combs))
        self.into_file(self.number, for_write, start_time)

    def into_file(self, number, for_write, start_time):
        with open('num_dict{number}.txt'.format(number=number), 'w', encoding='utf8') as file:
            for i in for_write:
                file.write(i + '\n')
        self.time_stop(start_time)

    @staticmethod
    def time_stop(start):
        final = time.time() - start
        print(f'Completed in:{final: .2f}')


CombosGenerator()