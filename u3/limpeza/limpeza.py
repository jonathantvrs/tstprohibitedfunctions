# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
"""
def troca(valor):
    v = list(str(valor))
    
    for i in range(len(v)):
        if v[i] == '.':
            v[i] 
    return str(v)
"""

servico = int(raw_input())

if servico == 1:
    tamanho_tanque = int(raw_input())
    custo_limpeza = 80 * tamanho_tanque
    print "R$ " + str(custo_limpeza) + ",00"
    if custo_limpeza >= 200:
        print "Brinde!"
elif servico == 2:
    tamanho_tanque = int(raw_input())
    custo_limpeza = 50 * tamanho_tanque
    print "R$ " + str(custo_limpeza) + ",00"
    if custo_limpeza >= 200:
        print "Brinde!"
elif servico == 3:
    print "R$ 50,00"
