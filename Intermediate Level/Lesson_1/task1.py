import argparse


class Extract:
    def read_file(self, domain):
        with open('base.txt', 'r', encoding='utf8') as file:
            content = file.readlines()
            with open('email_{dom}.txt'.format(dom=domain), 'w', encoding='utf8') as file_ch:
                for string in content:
                    string_spl = string.split(':')
                    if string_spl[0][-1:-len(domain) - 1:-1] == domain[-1::-1]:
                        file_ch.write(string)
        return print('done!')


parser = argparse.ArgumentParser(description='Выделяет emailы с опредленным доменом и переводит из файла в другой')
parser.add_argument('domain')
args = parser.parse_args()
print(args)

Extract().read_file(args.domain)
