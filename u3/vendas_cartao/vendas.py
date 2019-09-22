# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

valor = float(raw_input("Valor (R$): "))
tipo = raw_input("(D)ébito ou (C)rédito: ")

if tipo.lower() == "c":
    valor_liquido = valor - (valor * 0.05)

    print "Valor líquido a receber: %.2f" % valor_liquido
elif tipo.lower() == "d":
    valor_liquido = valor - (valor * 0.03)
    print "Valor líquido a receber: %.2f" % valor_liquido
else:
    print "Tipo incorreto. Tente novamente." 
