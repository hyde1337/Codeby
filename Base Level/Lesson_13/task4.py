def digtext(func):
    def wrapped(*string):
        middle = '|'.join(*string)
        print('+-' * len(*string) + '+\n' + '|' + middle + '|\n' + '+-' * len(*string) + '+')
        return func
    return wrapped


@digtext
class TextPrint:
    def __init__(self, text):
        self.text = text
        self.print_text()

    def print_text(self):
        print(self.text)


x = TextPrint('TESTEST')
