# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

quantidade_lidos = int(raw_input())

aceitos, descartados, letras_diferentes = 0, 0, 0
numeros_aceitos, numeros_descartados = "", ""

for i in range(quantidade_lidos):
    numero = raw_input()
    for j in range(len(numero)):
        if int(numero[j]) == j:
            descartados += 1
            numeros_descartados += "\n" + numero
            letras_diferentes = 0
            break
        else:
            letras_diferentes += 1
    if letras_diferentes == len(numero):
        aceitos += 1
        numeros_aceitos += numero + "\n"
        letras_diferentes = 0

print "---"
print "%d aceito(s)\n%s%d descartado(s)%s" % (aceitos, numeros_aceitos, descartados, numeros_descartados)
