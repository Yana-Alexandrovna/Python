#Задача №19. Решение в группах
#Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K –
#положительное число.
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]
#Примечание: Пользователь может вводить значения списка или список задан изначально.

N = int(input('Введите количество элементов в массиве: '))
print('Введите элементы:')
list_1 = [int(input()) for item in range(N)]
X = int(input('Введите число Х: '))
for i in range(X):
    list_1.append(list_1.pop(0))
print(list_1)