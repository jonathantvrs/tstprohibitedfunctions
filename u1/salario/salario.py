# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

salario_bruto = float(raw_input())
horas_trabalhadas = int(raw_input())

hora_bruta = salario_bruto / horas_trabalhadas

desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

desconto_total = desconto_ir + desconto_inss + desconto_sindicato

salario_liquido = salario_bruto - desconto_total
hora_liquida = salario_liquido / horas_trabalhadas

print "Salário Bruto =", salario_bruto
print "Hora Bruta =", hora_bruta
print "Desconto IR =", desconto_ir
print "Desconto INSS =", desconto_inss
print "Desconto Sindicato =", desconto_sindicato
print "Salário Líquido =", salario_liquido
print "Hora Líquida =", hora_liquida
