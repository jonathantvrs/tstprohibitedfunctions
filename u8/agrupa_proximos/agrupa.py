# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def agrupa_proximos(lista, valor, criterio):
    lista_agrupados = []

    for i in range(len(lista)):
        if abs(valor - lista[i]) < criterio:
            lista_agrupados.append(lista[i])

    return lista_agrupados
