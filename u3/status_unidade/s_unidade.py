# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

quantidade_minitestes = int(raw_input())

if quantidade_minitestes == 1:
    media = float(raw_input())
    print media
    print "Aluno ainda não aprovado na unidade"
elif quantidade_minitestes == 2:
    nota_um = float(raw_input())
    nota_dois = float(raw_input())
    
    media = (nota_um + nota_dois) / 2.0
    
    print media
    
    if media < 6:
        print "Aluno ainda não aprovado na unidade"
    else:
        print "Aluno aprovado na unidade"
else:
    nota_um = float(raw_input())
    nota_dois = float(raw_input())
    nota_tres = float(raw_input())
    
    media = (nota_um + nota_dois + nota_tres) / 3.0
    media -= 0.5
    
    print media    
    
    if media < 6:
        print "Aluno ainda não aprovado na unidade"
    else:
        print "Aluno aprovado na unidade"
    
    
