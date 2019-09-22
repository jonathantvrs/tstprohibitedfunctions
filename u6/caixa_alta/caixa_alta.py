# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def custom_split(lista, parametro):
    string_aux = ""
    palavras_frase = [] 

    for c in lista:
        if c != " ":
            string_aux += c
        else:
            palavras_frase.append(string_aux)
            string_aux = ""
    if string_aux != " " or string_aux != parametro:
        palavras_frase.append(string_aux)

    return palavras_frase

def caixa_alta(frase):
    palavras_frase = custom_split(frase, " ")   
    new_phrase = ""
    
    for i in range(len(palavras_frase)):
        if i + 1 < len(palavras_frase):
            if len(palavras_frase[i]) == 1:
                new_phrase += palavras_frase[i].lower() + " " 
            else:
                new_phrase += palavras_frase[i].capitalize() + " "
        else:
            if len(palavras_frase[i]) == 1:
                new_phrase += palavras_frase[i].lower()
            else:
                
    return new_phrase

print caixa_alta("A primeira letra de cada palavra")
print caixa_alta("a PrimeirA letra de Cada pAlavra")
print caixa_alta("Primeira s de cada S")
#print caixa_alta()
