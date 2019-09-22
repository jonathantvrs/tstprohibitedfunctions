# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

print "Análise da Turma"
print "==="

quantidade_aprovados = int(raw_input("Número de aprovados? "))
quantidade_reprovados = int(raw_input("Número de reprovados? "))

total_alunos = quantidade_aprovados + quantidade_reprovados

percentual_aprovados = quantidade_aprovados * 100.0 / total_alunos 
percentual_reprovados = quantidade_reprovados * 100.0 / total_alunos

print "---"

print "Total de alunos na turma: %d" % (total_alunos)
print "Aprovados: %d = %.1f%%" % (quantidade_aprovados, percentual_aprovados)
print "Reprovados: %d = %.1f%%" % (quantidade_reprovados, percentual_reprovados)
