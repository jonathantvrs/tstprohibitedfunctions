# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

salario_base = float(raw_input())
quantidade_dias_trabalhados = int(raw_input())
custo_diario_transporte = float(raw_input())

print "O salário base é R$ %.2f" % salario_base

custo_transporte = custo_diario_transporte * quantidade_dias_trabalhados
percentual_custo_transporte = (custo_transporte / salario_base) * 100
fgts_empregador = salario_base * 0.08
inss_empregador = salario_base * 0.12

if salario_base <= 1317.07:
    inss_empregado = salario_base * 0.08
elif 1317.08 <= salario_base < 2195.12:
    inss_empregado = salario_base * 0.09
else:
    inss_empregado = salario_base * 0.11

if percentual_custo_transporte > 6:
    vale_transporte_empregador = custo_transporte - (salario_base * 0.06) 
    vale_transporte_empregado = salario_base * 0.06     
else:
    vale_transporte_empregado = 0
    vale_transporte_empregador = 0

salario_liquido = salario_base - vale_transporte_empregado - inss_empregado
custo_empregador = salario_base + inss_empregador + fgts_empregador + vale_transporte_empregador

print "O custo mensal para o empregador é de R$ %.2f" % custo_empregador
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido

