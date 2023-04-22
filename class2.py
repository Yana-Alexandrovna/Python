#5. Создать класс прямоугольник - Rectangle.
#   Метод __init__ принимает две точки - левый верхний и правый нижний угол. 
#   Каждая точка представлена экземпляром класса Point.
#   Реализуйте методы вычисления площади и периметра прямоугольника.
#
#6. Добавьте в класс Rectangle метод has_point.
#   Метод принимает точку на плоскости и возвращает True, если точка находиться внутри прямоугольника и False в противном случае

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y



class Rectangle:
    def __init__(self, left_up: Point, right_down: Point):
        self.left_up = left_up
        self.right_down = right_down

    def get_perimetr(self):
        return(abs(self.left_up.x - self.right_down.x)+abs(self.left_up.y - self.right_down.y))*2

    def get_square(self):
        return(abs(self.left_up.x - self.right_down.x)*abs(self.left_up.y - self.right_down.y))
    
    def has_point(self):
        point_x = int(input('x = '))
        point_y = int(input('y = '))
        if self.left_up.x <= point_x <= self.right_down.x and self.left_up.y <= point_y <= self.right_down.y:
            return True
        else:
            return False


point1 = Point(5,6)
point2 = Point(2,3)
rect = Rectangle(point1,point2)

print(rect.get_perimetr())
print(rect.get_square())
print(rect.has_point())