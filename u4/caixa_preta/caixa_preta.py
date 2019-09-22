# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

quantidade_de_medicoes = int(raw_input())

validacao = True
medicoes = []
dados_validos = 0
for i in range(quantidade_de_medicoes):
    medicoes = raw_input().split(" ")
    peso, combustivel, altitude = int(medicoes[0]), int(medicoes[1]), int(medicoes[2])
    if validacao:
        if peso < 0:
            dados_validos = 3 * i
            validacao = False
            print "dado inconsistente. peso negativo."
        elif combustivel < 0:
            dados_validos = 3 * i + 1
            validacao = False
            print "dado inconsistente. combustível negativo."
        elif altitude < 0:
            dados_validos = 3 * i + 2
            validacao = False
            print "dado inconsistente. altitude negativa."
        else:
            dados_validos = quantidade_de_medicoes * 3
print dados_validos, "dados válidos."
