import click


@click.command()
@click.argument('domain')
class Extractor:
    def __init__(self, domain):
        self.domain = domain
        self.read_file()

    def read_file(self):
        with open('base.txt', 'r', encoding='utf8') as file:
            content = file.readlines()
            self.ext_and_write(self.domain, content)

    @staticmethod
    def ext_and_write(domain, content):
        with open('email_{dom}.txt'.format(dom=domain), 'w', encoding='utf8') as file_ch:
            for string in content:
                string_spl = string.split(':')
                if string_spl[0][-1:-len(domain) - 1:-1] == domain[-1::-1]:
                    file_ch.write(string)
    click.echo("Done!")


Extractor()
