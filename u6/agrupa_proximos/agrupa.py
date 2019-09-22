# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def agrupa_proximos(lista, valor, criterio):
    lista_proximos = []

    for i in range(len(lista)):
        if abs(lista[i] - valor) < criterio:
            lista_proximos.append(lista[i])
    
    return lista_proximos       


l = [1,2,3,4,8,22,3,5]
print agrupa_proximos(l, 4, 2)
#assert agrupa_proximos(l, 4, 2) == [3,4,3,5] 
