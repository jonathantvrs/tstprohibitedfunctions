# -*- coding: utf-8 -*-
# jonathan.tavares.silva
# 118210631

media_mensal_ssp = float(raw_input())


sequencia = ""	
while True:
    dados = raw_input().split()
    
    avg = 0

    if dados[0] != "fim":
        for dado in dados:
            avg += int(dado)
        avg /= float(len(dados))
 
        if avg > media_mensal_ssp / 2: 
            if avg > media_mensal_ssp:
                for i in range(len(dados)):
                    if (i + 1) < len(dados):       
                        sequencia += dados[i] + " "
                    else:
                        sequencia += dados[i]
                print sequencia
                sequencia = ""
        else: break
    else: break 
