# задача 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

# class Data:
#     def __init__(self, day_month_year):
#         # self.day = day
#         # self.month = month
#         # self.year = year
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         my_date = []
#
#         for i in day_month_year.split():
#             if i != '-': my_date.append(i)
#
#         return int(my_date[0]), int(my_date[1]), int(my_date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2022 >= year >= 0:
#                     return f'Всё верно'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Data.extract(self.day_month_year)}'
#
# today = Data('11 - 1 - 2001')
# print(today)
# print(Data.valid(11, 11, 2023))
# print(today.valid(11, 13, 2011))
# print(Data.extract('11 - 09 - 2022'))
# print(today.extract('28 - 09 - 2022'))
# print(Data.valid(1, 11, 2000))

# задача 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# def div():
#     try:
#         user_num_1 = int(input('Введите делимое: '))
#         user_num_2 = int(input('Введите делитель: '))
#         if user_num_2 == 0:
#             raise OwnError("Делить на 0 нельзя!")
#         else:
#             res = user_num_1 / user_num_2
#             return res
#     except ValueError:
#         return "Введите числo!"
#     except OwnError as err:
#         return err
#
# print(div())

# задача 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится
# на экран.

# class NotNumberError(Exception):
#     def __init__(self, text):
#         self.text = text
#
#     def __str__(self):
#         return self.text
#
#
# if __name__ == '__main__':
#     my_list = []
#
#     while True:
#         user_input = input("Введите число для заполнения списка, или 'stop' для выхода: ")
#
#         if user_input == "stop":
#             break
#
#         try:
#             if not user_input.isdigit():
#                 raise NotNumberError(f"'{user_input}' напишите только числа")
#
#             my_list.append(int(user_input))
#         except NotNumberError as e:
#             print(e)
#
#     print(my_list)


# задача 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# задача 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# задача 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

# class StoreMashines:
#
#     def __init__(self, name, price, quantity, number_of_lists, *args):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.numb = number_of_lists
#         self.my_store_full = []
#         self.my_store = []
#         self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
#
#     def __str__(self):
#         return f'{self.name} цена {self.price} количество {self.quantity}'
#
#     # @classmethod
#     # @staticmethod
#     def reception(self):
#         # print(f'Для выхода - Q, продолжение - Enter')
#         # while True:
#         try:
#             unit = input(f'Введите наименование ')
#             unit_p = int(input(f'Введите цену за ед '))
#             unit_q = int(input(f'Введите количество '))
#             unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
#             self.my_unit.update(unique)
#             self.my_store.append(self.my_unit)
#             print(f'Текущий список -\n {self.my_store}')
#         except:
#             return f'Ошибка ввода данных'
#
#         print(f'Для выхода - Q, продолжение - Enter')
#         q = input(f'---> ')
#         if q == 'Q' or q == 'q':
#             self.my_store_full.append(self.my_store)
#             print(f'Весь склад -\n {self.my_store_full}')
#             return f'Выход'
#         else:
#             return StoreMashines.reception(self)
#
# class Printer(StoreMashines):
#     def to_print(self):
#         return f'to print smth {self.numb} times'
#
# class Scanner(StoreMashines):
#     def to_scan(self):
#         return f'to scan smth {self.numb} times'
#
# class Copier(StoreMashines):
#     def to_copier(self):
#         return f'to copier smth  {self.numb} times'
#
# unit_1 = Printer('hp', 2000, 5, 10)
# unit_2 = Scanner('Canon', 1200, 5, 10)
# unit_3 = Copier('Xerox', 1500, 1, 15)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
# print(unit_1.to_print())
# print(unit_3.to_copier())

# задача 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

import math

class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s+%sj)' % (self.a, self.b)

    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return MyComplex(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)

z1 = MyComplex(1, 2)
z2 = MyComplex(2, 3)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)

# проверка
# print(complex(1, 2) + complex(2, 3))
# print(complex(1, 2) * complex(2, 3))