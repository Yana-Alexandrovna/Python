#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
#Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.

a,b,c = int(input()),int(input()),int(input())
if(a+b)>c and (a+c)>b and (b+c)>a:
    print ('Существует')
else:
    print ('Не существует')