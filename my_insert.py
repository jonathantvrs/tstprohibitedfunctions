# -*- coding: utf-8 -*-
# author: jonathan

def custom_insert(l, pos, elem):
    aux_list = []
    
    for i in range(len(l)):
        aux_list.append(l[i])    
    
    while len(l) > 0:
        l.pop()

    for i in range(len(aux_list)):
        if i == pos:
            l.append(elem)
            l.append(aux_list[i])
        else:
            l.append(aux_list[i])

    return l

# assert custom_insert([1, 2, 3, 4, 5], 0, 0) == [0, 1, 2, 3, 4, 5]
# assert custom_insert(["Jonathan", "Wesley"], 1, "Everton") == ["Jonathan", "Everton" ,"Wesley"]
