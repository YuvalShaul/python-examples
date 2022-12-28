

from hashlib import new


my_num = 5

def change_num(new_value):
    global my_num
    my_num = new_value
    pass


change_num(7)
print(my_num)

