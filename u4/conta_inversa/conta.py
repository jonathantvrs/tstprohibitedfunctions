# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

palavra = raw_input()

caracteres_coincidentes = 0
palavra_invertida = ""
for i in range(len(palavra) - 1, -1, -1):
    palavra_invertida += palavra[i]
for i in range(len(palavra)):
    if palavra_invertida[i] == palavra[i]:
        caracteres_coincidentes += 1

print "A palavra %s contém %d caractere(s) coincidente(s) com a sua inversa." % (palavra, caracteres_coincidentes) 
