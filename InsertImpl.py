# -*- coding: utf-8 -*-
# author: jonathan

def custom_insert(l, position, element):
	
	l.append(element)
	
	for i in range(len(l) - 1, position, -1):
		l[i], l[i - 1] = l[i - 1], l[i]
	
	return l

	    
assert custom_insert([1, 2, 3, 4, 5], 0, 0) == [0, 1, 2, 3, 4, 5]
assert custom_insert(["Jonathan", "Wesley"], 1, "Everton") == ["Jonathan", "Everton" ,"Wesley"]
