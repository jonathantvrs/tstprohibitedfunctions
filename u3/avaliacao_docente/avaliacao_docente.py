# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

numero_semestres = int(raw_input())
atividades_ensino = int(raw_input())
producao_intelectual = int(raw_input())
atividades_orientacao = int(raw_input())
atividades_administrativas = int(raw_input())

if numero_semestres >= 4: 
    if atividades_ensino >= 320 and producao_intelectual >= 100 and atividades_orientacao >= 20:
    
        media_semestres = (atividades_ensino + producao_intelectual + atividades_orientacao + atividades_administrativas) / 4
    
        if media_semestres > 140:
            print "Promoção deferida. Parabéns!"
        else:
            print "Promoção indeferida. Média insuficiente."
    else:
        print "Promoção indeferida. Pontuação mínima não alcançada."
else:
    print "Promoção indeferida. Número de semestres insuficiente."
