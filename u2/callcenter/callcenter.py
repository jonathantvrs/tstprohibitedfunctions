# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

atendimento_um = int(raw_input())
atendimento_dois = int(raw_input())
atendimento_tres = int(raw_input())
atendimento_quatro = int(raw_input())
atendimento_cinco = int(raw_input())
atendimento_seis = int(raw_input())
atendimento_sete = int(raw_input())

total_atendimentos = atendimento_um + atendimento_dois + atendimento_tres + atendimento_quatro + atendimento_cinco + atendimento_seis + atendimento_sete

print "Total: %d" % total_atendimentos 
print "Média: %.2f" % (total_atendimentos / 7.0)
