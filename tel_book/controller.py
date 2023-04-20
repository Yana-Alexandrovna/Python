import view
import database

def main():
    while True:
        op = view.get_op()
        if op == 1:
            data_worker = view.get_data()
            database.add_data(data_worker)
        if op == 2:
            data_str = view.get_data_worker()
            view.find_person(data_str)
        if op == 3:
            data_str = view.get_data_worker()
            user_lst, full_lst = database.select_data_person(data_str)
            num = view.get_number()
            database.delete_person(user_lst, full_lst, num)
        if op == 4:
            data_str = view.get_data_worker()
            user_lst, full_lst = database.select_data_person(data_str)
            num = view.get_number()
            new_worker = view.get_data()
            database.change_person(user_lst, full_lst, num, new_worker)
        if op == 5:
            print('Выход')
            break