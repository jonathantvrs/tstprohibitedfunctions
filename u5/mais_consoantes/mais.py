# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

conta_palavras, quantidade_consoantes, quantidade_vogais = 0, 0, 0
while quantidade_consoantes <= quantidade_vogais:
    quantidade_vogais, quantidade_consoantes = 0, 0
    conta_palavras += 1
   
    palavra = raw_input().lower()
    
    for c in palavra:
        if c in "aeiou":
            quantidade_vogais += 1
        else:
            quantidade_consoantes += 1

print conta_palavras     
