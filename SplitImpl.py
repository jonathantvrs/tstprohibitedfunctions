# -*-  coding: utf-8  -*-
# author: jonathantvrs

def fsplit(string, separator=" "):
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
    elements = []
    aux_str = ""
    for s in string:
        if s != separator:
            aux_str = aux_str + s
        else:
            elements.append(aux_str)
            aux_str = ""
    
    if aux_str != "" or aux_str != separator:
        elements.append(aux_str)
    
    return elements

