#Создайте список из случайных чисел. Найдите второй максимум.
#a = [1, 2, 3] Первый максимум = 3, второй = 2

import random

N = int(input('Введите количество элементов в массиве: '))
list_1 = [random.randint(-50, 50) for item in range(N)]
print(list_1)
list_1.sort()
print(list_1[-2])
