# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

dia_um = int(raw_input())
dia_dois = int(raw_input())
dia_tres = int(raw_input())
dia_quatro = int(raw_input())
dia_cinco = int(raw_input())

minutos_perdidos = dia_um + dia_dois + dia_tres + dia_quatro + dia_cinco
media_minutos_dia = minutos_perdidos / 5.0
porcentagem_da_semana = minutos_perdidos * 100 / 7200.0
quantidade_episodios_house = minutos_perdidos / 50

print "Você perdeu %d min na semana (média de %.1f min por dia)." % (minutos_perdidos, media_minutos_dia)
print "Isso significa %.2f%% da sua semana produtiva." % porcentagem_da_semana
print "Daria para assistir %d episódio(s) de House." % quantidade_episodios_house
