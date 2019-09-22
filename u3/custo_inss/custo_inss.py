# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

valor_salario = float(raw_input())

contribuicao_empregador = valor_salario * 0.12

if valor_salario < 1317.08:
    contribuicao_empregado = valor_salario * 0.08
elif 1317.08 <= valor_salario < 2195.13:
    contribuicao_empregado = valor_salario * 0.09
else:
    contribuicao_empregado = valor_salario * 0.11

print "O valor da contribuição do INSS a ser pago pelo empregador é de R$ %.2f" % contribuicao_empregador
print "O valor da contribuição do INSS a ser pago pelo empregado é de R$ %.2f" % contribuicao_empregado
