# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_divisivel = int(raw_input())
tamanho_sequencia = int(raw_input())

quantidade_divisiveis = 0.0
for i in range(tamanho_sequencia):
    numero = int(raw_input())
    if numero % numero_divisivel == 0:
        quantidade_divisiveis += 1

porcentagem_divisiveis = quantidade_divisiveis / tamanho_sequencia * 100

print "%d (%.1f%%)" % (quantidade_divisiveis, porcentagem_divisiveis)
