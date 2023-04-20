def get_op():
    op = int(input("1 - импорт.\n 2 - экспорт.\n 3 - удалить.\n 4 - изменить.\n 5 - выход.\n"))
    return op               

def get_data():
    print ('Введите данные')
    name = input('имя ')
    surname = input('фамилия ')
    telephone = input('телефон ')
    data_str = name + ' ' + surname + ' ' + telephone + "\n"
    return data_str

def get_data_worker():
    data = input("Введите данные о пользователе, которые будем смотреть: ")
    return data

def get_number():
    num = int(input("Выберете строчку для изменения: "))
    return num

def find_person(data_str):
    with open('file.txt','r', encoding = 'utf-8') as f:
        lst_str = f.readlines()
        for worker in lst_str:
            if data_str in worker:
                print(worker)
