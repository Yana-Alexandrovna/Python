# Задача №23. Решение в группах
#Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента
#с предыдущим номером)
#Input: [0, -1, 5, 2, 3]
#Output: 2 (-1 < 5, 2 < 3)
#Примечание: Пользователь может вводить значения списка или список задан изначально.


N = int(input('Введите количество элементов в массиве: '))
print('Введите элементы:')
list_1 = [int(input()) for item in range(N)]
count = 0 
for i in range(len(list_1)-1):
    if list_1[i] < list_1[i+1]:
        count +=1
print(count)
