# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

unidade = int(raw_input('Unidade? '))
media = float(raw_input('Média de aprovação na unidade? '))

unidade += 1
print '\nO aluno vai para a unidade %d com média %.1f.' % (unidade, media)
