# -*-  coding: utf-8  -*-
# author: jonathantvrs

def fin(l, parameter):
    """Returns True if parameter was found in l. 

    Search for element in a list or string and
    return True if was found

    Parameters
    ----------
    l : list | str
        structure where the parameter will be searched
    parameter : str
        element that will be sought
        
    Return
    ------
    found : bool
        True if parameter was found in the list 
    """
    found = False
    for e in l:
        if e == parameter:
            found = True
    
    return found