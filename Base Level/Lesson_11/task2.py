dol_to_rub = float(input('Введите курс доллара к рублю: '))
dollars = float(input('Введите введите количесто долларов: '))
course = dollars * dol_to_rub
round(course, 2)

print(f'По курсу {dol_to_rub} рублей за доллар вы получите {course} рублей')
print('По курсу %.2f рублей за доллар вы получите %.2f рублей' % (dol_to_rub, course))
print('По курсу {} рублей за доллар вы получите {} рублей'.format(dol_to_rub, course))
