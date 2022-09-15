# Задача 1
# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

my_f = open('test.txt', 'w', encoding='utf-8')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break
my_f.close()
my_f = open('test.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(content)
my_f.close()

# Задача 2
# Создать текстовый файл(не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

my_file = open('test_hw5.txt', 'r', encoding='utf-8')
content = my_file.read() # прочтет файл
print(f'Содержимое файла: \n {content}')
my_file = open('test_hw5.txt', 'r', encoding='utf-8')
content = my_file.readlines() # подсчитает кол-во строк
print(f'Количество строк в файле - {len(content)}')
my_file = open('test_hw5.txt', 'r', encoding='utf-8')
content = my_file.readlines()
for i in range(len(content)): # подсчитает кол-во символов в строке циклом
    print(f'Количество символов {i + 1} строки - {len(content[i])}')
my_file = open('test_hw5.txt', 'r', encoding='utf-8')
content = my_file.read()
content = content.split() # подсчитает кол-во слов
print(f'Общее количество слов - {len(content)}')
my_file.close()

# Задача 3
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

my_file = open('test_hw5-1.txt', 'r', encoding='utf-8')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file.close()
with open('test_hw5-1.txt', 'r', encoding='utf-8') as my_file:
    salary = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000.00:
           poor.append(i[0]) # Метод append добавляет элемент в конец списка.
        salary.append(i[1])
print(f'Оклад меньше 20000.00 {poor}, средний оклад {sum(map(float, salary)) / len(salary)}')

# Задача 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 # Two — 2 # Three — 3 # Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
rus_new = []
with open(r'task1\test_hw_5.txt', 'r', encoding='utf-8') as f:
    # f_1 = f.read()
    # list = f_1.split("\n")
    for i in f:
        i = i.split(' ', 1)
        rus_new.append(rus[i[0]] + '  ' + i[1])
    print(rus_new)

with open('file_hw_5.txt', 'w', encoding='utf-8') as f_2:
    f_2.writelines(rus_new)

# Задача 5
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def summary():
 try:
  with open('test_5.txt', 'w+') as f:
   line = input('Введите цифры через пробел \n')
   f.writelines(line) # Метод file.writelines() пишет список строк в файл
   my_numb = line.split() # Функция split () используется для разделения строки на список строк на основе разделителя.
   print(sum(map(int, my_numb)))
 except ValueError:
  print('Введите цифры')
summary()

# Задача 6
# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
#
subj = {}
with open('test_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')

# Задача 7
# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

# import json
# profit = {}
# pr = {}
# prof = 0
# prof_aver = 0 # aver - средний
# i = 0
# with open('test_7.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         name, firm, earning, damage = line.split() # earning, damage - заработок, ущерб
#         profit[name] = int(earning) - int(damage)
#         if profit.setdefault(name) >= 0: # setdefault - установить значение по умолчанию
#             prof = prof + profit.setdefault(name)
#             i += 1
#     if i != 0:
#         prof_aver = prof / i
#         print(f'Прибыль средняя - {prof_aver:.2f}')
#     else:
#         print(f'Прибыль средняя - отсутствует. Все работают в убыток')
#     pr = {'средняя прибыль': round(prof_aver)}
#     profit.update(pr)
#     print(f'Прибыль каждой компании - {profit}')
#
# with open('file_7.json', 'w', encoding='utf-8') as write_js:
#     json.dump(profit, write_js)
#
#     js_str = json.dumps(profit)
#     print(f'Создан файл с расширением json со следующим содержимым: \n'
#           f'{js_str}')


