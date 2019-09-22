# -*- coding: utf-8 -*-
# jonathan.tavares.silva
# 118210631
import locale

media_mensal_secretaria = float(raw_input())


sequencia = ""	
while True:
    dados = raw_input().split()
    
    avg = 0.0

    if dados[0] != "fim":
        for dado in dados:
            avg += float(dado)
        avg /= float(len(dados))
 
        if avg > media_mensal_secretaria / 2.0: 
            if avg > media_mensal_secretaria:
                for i in range(len(dados)):
                    if (i + 1) < len(dados):       
                        sequencia += locale.format("%.1f", float(dados[i])) + " "
                    else:
                        sequencia += locale.format("%.1f", float(dados[i]))
                print sequencia
                sequencia = ""
        else: break
    else: break 
