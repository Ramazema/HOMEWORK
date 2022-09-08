# задача 1

li = [9, -30, [1, 8], "Hello", {"nike": "adidas", "joma": "bosco"}, (1, 2)]
for i in range (len(li)) : # определим длину списка с помощью функции len. Затем это значение передается функции range.
    print(f"Тип переменной в списке: {type(li[i])}")

# задача 2

li = input("Введите элементы списка: ").split()
li[:-1:2], li[1::2] = li[1::2], li[:-1:2]
print(li)

# задача 3

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input('Введите порядковый номер месяца в году (1..12): '))
if month == 12 or month == 1 or month == 2:
        print(f'Введенный номер месяца относится к сезону ' + seasons_dict.get(1))
        print(f'Введенный номер месяца относится к сезону ' + seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(f'Введенный номер месяца относится к сезону ' + seasons_dict.get(2))
    print(f'Введенный номер месяца относится к сезону ' + seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(f'Введенный номер месяца относится к сезону ' + seasons_dict.get(3))
    print(f'Введенный номер месяца относится к сезону ' + seasons_list[2])
# elif month == 9 or month == 10 or month == 11:
    print(f'Введенный номер месяца относится к сезону ' + seasons_dict.get(4))
    print(f'Введенный номер месяца относится к сезону ' + seasons_list[3])
else:
        print("Такого месяца не существует")

# задача 4

i = 0
li = input('Введите предложение: ').split()
for word in li:
    i += 1
    if len(str(word)) > 10:
        print(i,".", str(word)[0:10])
    else:
        print(i,".", word)

# задача 5

my_list = [7, 5, 3, 3, 2]
li = int(input('Введите число: '))
li = [li]
li_new = my_list + li
li_new.sort()
print(li_new)

# без сортировки:

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (0 - выход) "))
while digit != 0:
    for el in range(len(my_list)): # Функция len() в Python, считает количество элементов.
        # Range — это встроенная функция Python, которая возвращает итерируемый объект (range object), содержащий целые числа. С помощью функция range() можно сгенерировать последовательность чисел с определенным шагом — далее их можно легко перебирать с помощью цикла for.
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)  #  .insert() — это метод для вставки элемента в список.
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)  # Метод append() в Python добавляет элемент в конец списка.
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (0 - выход) "))

# задача 6

q = int(input("Введите необходимое количество товаров?\n\t Кол-во: "))
chr = "Название", "Цена", "Количество", "Ед.изм"
products, names, prices, Quantity, uoms = [], [], [], [], []
for i in range(q):
    print(f"Введите характеристики для товара № {i + 1}: ")
    name, price, quantity, uom = input("\tНазвание : "), input("\tЦена товара : "), input("\tКоличество : "), input("\tЕд.изм : ")
    products_up = (i + 1, {chr[0]: name, chr[1]: price, chr[2]: quantity, chr[3]: uom})
    products.append(products_up)
    names.append(products[i][1].get(chr[0]))
    prices.append(products[i][1].get(chr[1]))
    Quantity.append(products[i][1].get(chr[2]))
    uoms.append(products[i][1].get(chr[3]))
