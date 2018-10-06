# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_sum(elements, last_value=0):
    sum = 0

    for element in elements:
        sum += int(element)

    return sum + last_value

#        tests case
# list = raw_input().split()
# print custom_sum(list)
# assert custom_sum([1,2,3]) == 6
