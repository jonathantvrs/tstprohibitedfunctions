# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_banco = raw_input()

soma_pares = 0
soma_impares = 0
for i in range(len(numero_banco)):
    if i % 2 == 0:
        soma_pares += int(numero_banco[i]) 
    else:
        soma_impares += int(numero_banco[i])

digito_verificador = soma_pares * soma_impares % 11

if digito_verificador == 10:
    digito_verificador = 'X'

print "%s-%s" % (numero_banco, digito_verificador)
