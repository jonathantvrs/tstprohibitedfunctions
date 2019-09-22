# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

palavra, lista_palavras = raw_input(), []
while palavra != "fim":
    lista_palavras.append(palavra)

    palavra = raw_input()
    

caractere = raw_input()
parametro = int(raw_input())

tem_palavra = False
for i in range(len(lista_palavras)):
    conta_caractere = 0
    for c in lista_palavras[i]:
        if c == caractere:
            conta_caractere += 1
    if conta_caractere > parametro:
        print lista_palavras[i]
        tem_palavra = True

if not tem_palavra:
    print "Nenhuma palavra encontrada."
