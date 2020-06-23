import click


@click.command()
@click.argument('value')
class Converter:
    def __init__(self, value):
        self.value = value
        self.conv(self.value)

    @staticmethod
    def conv(value):
        rights = ['---', '--x', '-w-', 'r-x', 'r--', 'r-x', 'rw-', 'rwx']
        print('Калькулятор прав доступа:')
        for i in value:
            print(rights[int(i)], end='')
        print('\n')


Converter()
