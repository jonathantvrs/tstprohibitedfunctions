# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

nota_enem = int(raw_input())
creditos_concluidos = int(raw_input())

porcentagem_concluida = creditos_concluidos / 416.0 * 100

if nota_enem < 600 and (porcentagem_concluida < 20 or porcentagem_concluida > 90):
    print "Nenhuma condição satisfeita."
else:
    if nota_enem >= 600 and 20 <= porcentagem_concluida <= 90:
        print "Todas as condições satisfeitas."        
    elif nota_enem < 600 and 20 <= porcentagem_concluida <= 90:
        print "Condição ENEM não satisfeita."
    else:
        print "Condição CRÉDITOS não satisfeita."

