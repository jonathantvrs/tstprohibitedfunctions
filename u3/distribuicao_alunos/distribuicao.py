# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

unidade = int(raw_input())
deseja_pular = raw_input()
qtd_questoes = int(raw_input())

if deseja_pular == "sim" and qtd_questoes > 0:
    unidade += 1

if 1 <= unidade <= 4:
    print "O aluno deve assistir aula com o prof João."
elif 5 <= unidade <= 8:
    print "O aluno deve assistir aula com o prof Dalton."
else:
    print "O aluno deve assistir aula com o prof Jorge." 
     
