# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

limite_superior = float(raw_input())
nivel_atual = float(raw_input())

while nivel_atual < limite_superior:
    evento = raw_input().split()
    
    if evento[0] == "chuva":
        nivel_atual += int(evento[1])
    elif evento[0] == "afluente":
        nivel_atual += int(evento[1])
    else:
        if (nivel_atual - int(evento[1])) >= 0:
            nivel_atual -= int(evento[1])    

if nivel_atual >= limite_superior:
    print "Açude passou a liberar água."
    print "Nível: %.2f" % nivel_atual
