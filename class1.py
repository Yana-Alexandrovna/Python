#1.Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста.
#  Создать экземпляр и вывести информацию о человеке.
#2.Доработать предыдущий класс, чтобы вся информация о человеке была доступна для вызова str над экземпляром.
#3.Добавить метод greet, вызов которого будет выводить вконсоль информации о человеке в формате:
# "Привет! Меня зовут Петров Василий, мне 12 лет".
#4. Добавить атрибут grades, в котором будет храниться список оценок.
#Создать список учеников, заполняя оценки случайными числами и вывести информацию о них в порядке убывания среднего балла.
#Заполнение оценок и подсчет среднего балла вынести в отдельные методы.
from statistics import mean

class Human:
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades

    def __str__(self):
        return f'{self.name} {self.surname}, {self.age}'
    
    def greet(self):
        print(f"Привет, меня зовут {self.name} {self.surname}, мне {self.age} лет")

    def sred_bal(self):
        sred = mean(self.grades)
        return sred
    
    def __repr__(self):
        return f'{self.name} {self.surname}'


ivan = Human("Иван", "Иванов", 12, [4,3,5,2])
maks = Human("Макс", "Максин", 15, [5,5,4,3])
petr = Human("Петр", "Петров", 17, [5,5,4,5])
alexey = Human("Алексей", "Алексеев", 10, [5,2,5,2])

peoples = [ivan, maks, petr, alexey]
new_peop = sorted(peoples, key=lambda x:x.sred_bal(),reverse = True)

print(ivan)
ivan.greet()
print(ivan.sred_bal())
print(peoples)
print(new_peop)