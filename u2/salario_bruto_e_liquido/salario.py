# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

nome_funcionario = raw_input()
quantidade_horas_extras = float(raw_input()) 
valor_salario_minimo = float(raw_input())
valor_hora_extra = float(raw_input())

salario_hora_extra = quantidade_horas_extras * valor_hora_extra
salario_bruto = 4 * valor_salario_minimo + salario_hora_extra
imposto_e_roubo_inss = salario_bruto * 0.12
imposto_e_roubo_renda = salario_bruto * 0.20
salario_liquido = salario_bruto - imposto_e_roubo_inss - imposto_e_roubo_renda 


print "O Salário Bruto de %s é de R$ %.2f" % (nome_funcionario, salario_bruto)
print "O Salário Líquido de %s é de R$ %.2f" % (nome_funcionario, salario_liquido)
