# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def my_split(seq, parametro):
    elements = []
    string_aux = ""

    for element in seq:
        if element != parametro:
            string_aux += element
        else:
            elements.append(string_aux)
            string_aux = ""
    if string_aux != "" or string_aux != parametro:
        elements.append(string_aux)
    return elements

def conta_palavras(k, palavras): 
    lista_palavras = my_split(palavras, ":")

    quantidade_palavras_maior_que_k = 0
    for i in range(len(lista_palavras)):
        if len(lista_palavras[i]) >= k:
            quantidade_palavras_maior_que_k += 1

    return quantidade_palavras_maior_que_k

print conta_palavras(5, "zero:um:dois:tres:quatro:cinco")
