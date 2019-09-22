# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_aposta = int(raw_input()) 
cor_aposta = raw_input()
numero_sorteado = int(raw_input())
cor_sorteada = raw_input()

pontos = 0

if numero_aposta == numero_sorteado and cor_aposta == cor_sorteada:
    pontos = 150
elif numero_aposta == numero_sorteado:
    pontos = 100
elif cor_aposta == cor_sorteada:
    pontos = 50
    if numero_sorteado > numero_aposta:
        pontos += 30
    else:
        pontos += 50

print pontos 
