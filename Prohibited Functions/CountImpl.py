# -*-  coding: utf-8  -*-
# author: jonathantvrs

def fcount(l, parameter):
    """Returns number of occurrences of an element
    in the list or string. 

    Search for occurrences of an element in a list
    or string and counts them.

    Parameters
    ----------
    l : list | str
        structure to iterate
    parameter : str
        element that will be counted

    Return
    ------
    counter : int
        number of occurrences of the element 
    """
    counter = 0
    for e in l:
        if e == parameter:
            counter = counter + 1

    return counter
