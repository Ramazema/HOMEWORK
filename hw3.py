# задача 1

def division(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        return 'Нельзя делить на 0'
    except ValueError:
        return 'Вводите только цифры'
a = input('Введите делимое: ')
b = input('Введите делитель: ')
print(division(a, b))
# или:
def division(a, b):
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        return 'Нельзя делить на 0'
    except ValueError:
        return 'Вводите только цифры'
print(division(a = input('Введите делимое: '), b = input('Введите делитель: ')))

# задача 2

def parameters(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth}'
                 f'Город проживания: {city} Email: {email} Телефон: {phone}')
parameters(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: ')
)

# задача 3

def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)
print(my_func(12, 11, 1))

# mylist = [1, 4, 0, 3, 2]
# mylist.remove(max(mylist)) # убирает мах из списка
# mylist.remove(min(mylist)) # убирает min из списка
# print(mylist)

# задача 4

def my_func(x, y):
    return abs(x) ** -abs(y)
print(f'Возведение в степень: '
      f'{my_func(float(input("Основание степени Х: ")), int(input("Показатель степени Y: ")))}')

def my_func(x, y):
    for i in range(abs(y * (-1))):
        x *= x # x = x * x
    return 1 / x
print(my_func(-3, 1))

# задача 5

def exe_5():
    res = 0
    while True:
        numbers = input('Введите цифры через пробел или * для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма равна {res}. Выход')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите номер или *')
        print(f'Сумма равна {res}')
exe_5()

# задачи 6, 7

def int_func(text):
    return text.title()
def my_title(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)
output_1 = []
output_2 = []
for word in input('Введите слова из маленьких латинских букв, разделённые пробелом: ').split(' '):
    output_1.append(int_func(word))
    output_2.append(my_title(word))

print(f'Вариант1 Строка получается: {" ".join(output_1)}')
print(f'Вариант2 Строка получается: {" ".join(output_2)}')

