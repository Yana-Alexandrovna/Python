#Задача №37. Решение в группах
#Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
#Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
#Input: 2 -> 3 4
#Output: 4 3

#def m(b, a = ""):
#    a = a + input()
#    if b == 1:
#        return a
#    return m(b-1 , a)

#b = int(input())
#print(m(b)[::-1]) 

def m(b, a = ""):
    a = input()
    if b == 1:
        return a
    return m(b-1 , a) + a

b = int(input())
print(m(b)) 