#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#5
#1 2 3 4 5
#6
#-> 5


N = int(input('Введите количество элементов в массиве: '))
print('Введите элементы:')
list_1 = [int(input()) for item in range(N)]
X = int(input('Введите число Х: '))
min = abs(X - list_1[0])
index = 0
for i in range(1, N):
    count = abs(X - list_1[i])
    if count < min:
        min = count
        index = i
print(list_1[index])