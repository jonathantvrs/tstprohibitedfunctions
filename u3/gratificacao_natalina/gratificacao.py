# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

codigo = int(raw_input())

if codigo == 1:
    print "Deverá receber em dezembro R$ 25000.00."
elif codigo == 2:
    print "Deverá receber em dezembro R$ 15000.00."
elif codigo == 3:
    dias_faltosos = int(raw_input())
    if dias_faltosos > 0:
        gratificacao = (235 - dias_faltosos) * 2.0
        salario = gratificacao + 8000.00
    else:
        gratificacao = 500.00
        salario = gratificacao + 8000.00
    print "Valor da gratificação R$ %.2f." % gratificacao
    print "Deverá receber em dezembro R$ %.2f." % salario
elif codigo == 4:
    dias_faltosos = int(raw_input())
    if dias_faltosos > 0:
        gratificacao = (235 - dias_faltosos) * 1.0
        salario = gratificacao + 5000.00
    else:
        gratificacao = 300.00
        salario = gratificacao + 5000.00
    print "Valor da gratificação R$ %.2f." % gratificacao
    print "Deverá receber em dezembro R$ %.2f." % salario
elif codigo == 5:
    dias_faltosos = int(raw_input())
    if dias_faltosos > 0:
        gratificacao = (235 - dias_faltosos) * 0.7
        salario = gratificacao + 2800.00
    else:
        gratificacao = 200.00
        salario = gratificacao + 2800.00   
    print "Valor da gratificação R$ %.2f." % gratificacao
    print "Deverá receber em dezembro R$ %.2f." % salario
