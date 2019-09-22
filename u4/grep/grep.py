# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
def my_in(parametro, lista):
    for i in range(len(lista)):
        if i + 2 < len(lista):
            if parametro == lista[i] + lista[i + 1] + lista[i + 2]:
                return True
    return False



palavra = raw_input()

numero_frases = int(raw_input())

for i in range(numero_frases):
    frase = raw_input()
    
    if my_in(palavra, frase):
        print frase
    
    
