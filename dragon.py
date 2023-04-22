#1.Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы: рост, огнеопасность, цвет.
#Класс обеспечивает выполнение методов (dr — экземпляр класса) экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту
#2.экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:
#цвет меньший по алфавиту;
#рост - среднее арифметическое из двух округлённое до целого вниз,
#огнеопасность - большее из двух;
#3.Из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
#огнеопасности прибавляется остаток от деления огнеопасности на число;
#4.Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное значению атрибута огнеопасность;
#change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет
#str- возвращает строку:
#Dragon with height «рост», danger <огнеопасность> and color «цвет».
#repr- возвращaет строку:
#Dragon(‹рост>, <огнеопасность>, <цвет>)

class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color
    def __repr__(self) -> str:
        return "Я дракон, мой рост {self.height}, моя огнеопасность {self.danger}, мой цвет {self.color}"
    def __contrast_height__(self, other):
        if type(other) == Dragon:
            if self.height==other.height:
                return "они одного роста"
            else:
                return "у них разный рост"
    def __contrast_danger__(self, other):
        if type(other) == Dragon:
            if self.danger==other.danger:
                return "равные"
            else:
                return "зажарят по-разному"
    def __contrast_color__(self, other):
        if type(other) == Dragon:
            if self.color==other.color:
                return "они одного цвета"
            else:
                return "различие в цвете имеется"
    def __add__(self, other):
         import math
         color = min(self.color, other.color)
         height = math.floor((self.height + other.height)/2)
         danger = max(self.danger, other.danger)
         dr = Dragon(height, danger, color)
         return(dr)
    def __sub__(self, number):
         number = int(input('Введите число: '))
         self.height = self.height - int(self.height / number)
         self.danger = self.danger + self.danger % number
         return self
    def __str1__(self):
         string = input('Введите строку: ')
         print(string * self.danger)
    def change_color(self):
         new_color = input('Введите новый цвет: ')
         self.color = new_color
         return self



dr1 = Dragon(69, 5, "brown")
dr2 = Dragon(69, 5, "gray")
dr3 = Dragon(66, 10, "white")
dr4 = Dragon(35, 6, "gray")
dr5 = Dragon(50, 10, "brown")


