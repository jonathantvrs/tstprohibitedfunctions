# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import locale

quantidade_de_lidos = 0
soma_de_lidos, media_notas = 0.0, 0.0
abaixo_da_media, acima_da_media = "", ""
notas = []
while True:
    if soma_de_lidos < 100.0:
        numero = float(raw_input())
        
        quantidade_de_lidos += 1
        soma_de_lidos += numero
        
        notas.append(numero)
    else:
        media_notas = soma_de_lidos / quantidade_de_lidos
        break

for i in range(len(notas)):
    if notas[i] > media_notas:
        acima_da_media += "\n" + str(locale.format("%.2f", notas[i])) + " (" + str(i + 1) + "o)"
    else:
        abaixo_da_media += "\n" + str(locale.format("%.2f", notas[i])) + " (" + str(i + 1) + "o)"

print "Quantidade de números lidos: %d" % quantidade_de_lidos
print "Soma dos números lidos: %.2f" % soma_de_lidos
print "Média = %.2f" % media_notas

print "\nAbaixo da média%s\n" % abaixo_da_media

print "Acima da média%s" % acima_da_media
