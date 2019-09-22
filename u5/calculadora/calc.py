# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

while True:
    calculadora = raw_input().split()
    
    if len(calculadora) == 3: 
        operacao, p_operando, s_operando = int(calculadora[0]), int(calculadora[1]), int(calculadora[2])
    else:
        operacao = int(calculadora[0])

    if operacao == 1:
        print p_operando + s_operando
    elif operacao == 2:
        print p_operando - s_operando
    elif operacao == 3:
        print p_operando * s_operando
    elif operacao == 4:
        if s_operando == 0:
            print "Erro: Divisão por 0"
            break
        else:
            print p_operando / s_operando
    else:
        break
    
