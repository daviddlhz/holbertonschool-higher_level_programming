#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = 0
    uniq = set(my_list)
    for i in uniq:
        sum_list = sum_list + i
    return sum_list
