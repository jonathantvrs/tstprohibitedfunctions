# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_de_times = int(raw_input())
melhor_ataque, soma_gols = 0, 0


if numero_de_times >= 2:
    for i in range(numero_de_times):
        times = raw_input()
        gols = int(raw_input())
        soma_gols += gols       
        if gols > melhor_ataque:
            melhor_ataque = gols
            melhores_times = times
        elif gols == melhor_ataque:
            melhores_times += "\n" + times         

    media_gols = soma_gols / float(numero_de_times)

    print "Time(s) com melhor ataque (%d gol(s)):" % melhor_ataque
    print "%s" % melhores_times
    print ""
    print "Média de gols marcados: %.1f" % media_gols
