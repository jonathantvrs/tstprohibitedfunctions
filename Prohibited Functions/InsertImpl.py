# -*- coding: utf-8 -*-
# author: jonathantvrs

def finsert(l, pos, element):
	"""Returns the list with new element added at
	the defined position. 

	Add element to the end of the list and sort it
	to be in the position indicated.

    Parameters
    ----------
    l : list
        list where element will be added
    pos : int
        position that will be inserted
	element : int
        element that will be inserted 
        
    Return
    ------
    l : list
		list updated with new element
    """
	l.append(element)
	for i in range(len(l) - 1, pos, -1):
		l[i], l[i - 1] = l[i - 1], l[i]
	
	return l
