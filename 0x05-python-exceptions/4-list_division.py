#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    cnt = 0
    for i in range(list_length):
        try:
            cnt = my_list_1[i] / my_list_2[i]
        except(ValueError, TypeError):
            print("wrong type")
            cnt = 0
        except ZeroDivisionError:
            print("division by 0")
            cnt = 0
        except IndexError:
            print("out of range")
            cnt = 0
        finally:
            new_list.append(cnt)
    return new_list
