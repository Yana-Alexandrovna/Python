#Задача №11. Решение в группах
#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
#выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
#Input: 5
#Output: 6 

A = int(input("Введите число A: "))
F1 = 1
F2 = F1
F = F2
n = 3
while A > F:
    F = F1 + F2
    F1 = F2
    F2 = F
    n += 1
if A == F:
    print(n)
else:
    print(-1)