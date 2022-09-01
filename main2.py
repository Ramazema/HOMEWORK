# задача 1
x = 'хороший'
c = 'день'
print(x + ' ' + c)

b = '38'
d = ' в удаве попугаев'
print(b + d)

a = 859
m = 10
print(a + m)

# задача 2
time_sec = 34253  # или int(input('Введите число: '))
hours = time_sec//3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time_sec % 3600)//60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time_sec % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print('Количество полученных часов превышает количество часов в сутках, скорректируйте ввод.')
else:
    print(f'Значит, время: {hours_res}:{minutes_res}:{seconds_res}')

# задача 3
# n = 5
# nn = 55
# nnn = 555
# print(n + nn + nnn)

n = input('Введите число: ')
nn = int(n+n)
nnn = int(n+n+n)
n = int(n)
result = n+nn+nnn
print(result)

# задача 4
n = 34518
i = 0
while n > 0:
    last = n % 10
    print('последняя цифра', last)
    if last > i:
        i = last
    n = n // 10
print(i, 'самая большая цифра')

# задача 5
plus = int(input('Введите значение прибыли: '))
minus = int(input('Введите значение издержек: '))
people = int(input('Введите количество работников: '))
if plus > minus:
    print('Выручка больше издержек')
    clear_plus = plus - minus
    rent = clear_plus/plus
    print(rent, '- Рентабельность нашей выручки')
    clear_for_person = float(clear_plus/people)
    print(clear_for_person, '- Прибыль фирмы в расчете на одного сотрудника')
else:
    print('Фирма работает в убыток')

# задача 6
a = 2
b = 3
counter = 1 #счётчик дней
while a < b:
    a *= 1.1   #  a = a * b, or a *= b оператор присваивания
    counter += 1   # A += B or A = A + B оператор присваивания
print(f"На {counter}-й день спортсмен достиг результата — не менее {b} км")
















