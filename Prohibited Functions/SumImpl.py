# -*-  coding: utf-8  -*-
# author: jonathantvrs

def fsum(l, last_value=0):
    """Returns sum of integer list, possibly 
    added by an optional last value.

    Sum the list elements iterating one by one
    and at the end sum the result with an optional
    last value.

    Parameters
    ----------
    l : list
        integer list
    last_value : int, optional, default is 0
        last value to add to sum 
        
    Return
    ------
    sum : int
        sum of list elements with last_value
        
    """
    sum = 0
    for e in l:
        sum = sum + int(e)
    sum = sum + last_value

    return sum
