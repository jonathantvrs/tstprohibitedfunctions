# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

nome_jogador = raw_input()
idade_jogador = int(raw_input())

if 5 <= idade_jogador <= 7:
    categoria = 'Infantil A'
elif 8 <= idade_jogador <= 10:
    categoria = 'Infantil B'
elif 11 <= idade_jogador <= 13:
    categoria = 'Juvenil A'
elif 14 <= idade_jogador <= 17:
    categoria = 'Juvenil B'
elif 17 < idade_jogador:
    categoria = 'Senior'
else: 
    categoria = 'Não pode competir'

print "%s, %d anos, %s." % (nome_jogador, idade_jogador, categoria)
