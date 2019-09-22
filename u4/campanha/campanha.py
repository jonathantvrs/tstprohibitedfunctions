# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

pontos, vitorias, empates, derrotas = 0, 0, 0, 0
gols_pro, gols_contra, saldo_gols = 0, 0, 0
pontos_em_casa, pontos_fora = 0, 0
for i in range(10):
    jogo = raw_input()
    if jogo[5] == 'c':
        gols_pro += int(jogo[0])
        gols_contra += int(jogo[2])
        if int(jogo[0]) > int(jogo[2]):
            vitorias += 1
            pontos += 3
            pontos_em_casa += 3
        elif int(jogo[0]) == int(jogo[2]):
            empates += 1
            pontos += 1
            pontos_em_casa += 1
        else:
            derrotas += 1                
    elif jogo[5] == 'f':
        gols_pro += int(jogo[2])
        gols_contra += int(jogo[0])
        if int(jogo[0]) > int(jogo[2]):
            derrotas += 1
        elif int(jogo[0]) == int(jogo[2]):
            empates += 1
            pontos += 1
            pontos_fora += 1
        else:
            vitorias += 1
            pontos += 3
            pontos_fora += 3    
saldo_gols = gols_pro - gols_contra

print "%dv, %de, %dd" % (vitorias, empates, derrotas)
print "pontos: %d" % pontos
print "saldo: %d (%d pro, %d contra)" % (saldo_gols, gols_pro, gols_contra)
print "pontos em casa: %d" % pontos_em_casa
print "pontos fora: %d" % pontos_fora

