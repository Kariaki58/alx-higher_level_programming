#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_tuple = 0
    mult = 0
    for tup in my_list:
        mult += tup[0] * tup[1]
        sum_tuple += tup[1]
    return mult / sum_tuple
