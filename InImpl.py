# -*-  coding: utf-8  -*-
# author: jonathantvrs

def fin(l, parameter):
    """Returns a list of strings divided by separator. 

    Iterate the received string character by character
    and add the formed string to the list when it finds
    the separator.

    Parameters
    ----------
    string : str
        string to split
    separator : str, default is " " (space)
        parameter used to split the string 
        
    Return
    ------
    elements : list
        list containing the strings 
    """
    for e in l:
        if e == parameter:
            return True
    
    return False