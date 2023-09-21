# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def ind_in_diaposon(list1, maximum, minimum):
    list2 = []
    for i in range(len(list1) - 1):
        if list1[i] >= minimum and list1[i] <= maximum:
            list2.append(i)
    return list2

maximum = int(input('Введите максимум диапозона: '))
minimum = int(input('Введите минимум диапозона: '))

list1 = [1, 3, 4, 78, 20, 10, 7, 91]

list2 = ind_in_diaposon(list1, maximum, minimum)
print(list2)
