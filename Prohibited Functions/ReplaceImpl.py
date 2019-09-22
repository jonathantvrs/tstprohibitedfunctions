# -*-  coding: utf-8  -*-
# author: jonathantvrs

def freplace(seq, parameter, substitute):
    """Returns a new string exchanging the elements in 
    seq equal to the parameter for the substitute. 

    Iter element by element of the sequence replacing
    whatever equals parameter with substitute.

    Parameters
    ----------
    seq : str
        original string
    parameter : str
        string to be replaced
    substitute : str
        string that will replace 

    Return
    ------
    new_seq : str
        new string replaced 
    """
    new_seq = ""
    for e in seq:
        if e == parameter: 
            new_seq = new_seq + substitute 
        else: 
            new_seq = new_seq + e

    return new_seq