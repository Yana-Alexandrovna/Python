#Задача №39. Решение в группах
#Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
#число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
#Ввод: Вывод:
#7 3 3 2 12
#3 1 3 4 2 4 12
#6
#4 15 43 1 15 1 (каждое число вводится с новой строки)

def result (list_1, list_2, list_new):
    for i in list_1:
        if i not in list_2:
            list_new.append(i)    
    return list_new


num_1 = int(input("Введите количесво элементов в первом массиве: "))
list_1 = list()

for i in range(num_1):
    x = int(input("Введите элемент массива: "))
    list_1.append(x)

num_2 = int(input("Введите количесво элементов во втором массиве: "))
list_2 = list()

for i in range(num_2):
    x = int(input("Введите элемент массива: "))
    list_2.append(x)

list_new = list()
print(list_1, list_2, result(list_1, list_2, list_new))