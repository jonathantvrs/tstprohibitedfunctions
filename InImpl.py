# -*-  coding: utf-8  -*-
# author: jonathantvrs

def fin(l, parameter):
    """Returns True if parameter was found in l. 

    

    Parameters
    ----------
    l : list
        
    parameter : str
         
        
    Return
    ------
    found : bool
        list containing the strings 
    """
    found = False
    for e in l:
        if e == parameter:
            found = True
    
    return found