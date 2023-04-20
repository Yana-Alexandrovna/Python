def add_data(data_str):
    with open('file.txt','a', encoding = 'utf-8') as f:
        f.write(data_str)

def select_data_person(worker):
    user_lst = []
    with open('file.txt','r', encoding = 'utf-8') as f:
        full_lst = f.readlines()
        for count, line in enumerate(full_lst):
            if worker in line:
                user_lst.append(line)
                print(f"{count+1} {line}")
    return user_lst, full_lst


def delete_person(user_lst, full_lst, num):
    with open("file.txt", 'w', encoding = 'utf-8') as f:
        for line in full_lst:
            if user_lst[num-1]!=line:
                f.write(line)
    print('готово')


def change_person(user_lst, full_lst, num, new_worker):
    with open("file.txt", 'w', encoding = 'utf-8') as f:
        for line in full_lst:
            if user_lst[num-1]!=line:
                f.write(line)
            else:
                f.write(new_worker)
    print('готово')




