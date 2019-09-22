# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

agenda_nomes = []
agenda_telefones = []

def inserir_contato(quantidade, agenda_nomes, agenda_telefones):
    for i in range(quantidade):
        nome = raw_input()
        numero = raw_input()

        agenda_nomes.append(nome)
        agenda_telefones.append(numero)
        
        for i in range(len(agenda_nomes) - 1, -1, -1):
            if agenda_nomes[i] > nome:
                agenda_nomes[i], agenda_nomes[i + 1] = nome, agenda_nomes[i] 
                agenda_telefones[i], agenda_telefones[i + 1] = numero, agenda_telefones[i]

def buscar_contato(nome, agenda_nomes, agenda_telefones):
    quantidade_achados = 0
    for i in range(len(agenda_nomes)):
        if nome == agenda_nomes[i]:
            print "Nome: %s" % agenda_nomes[i]
            print "Fone: %s" % agenda_telefones[i]
            print "----------"
            
            quantidade_achados += 1
    
    if quantidade_achados == 0:
        print "Nome inexistente"
        print "----------"
            

def imprimir_agenda(agenda_nomes, agenda_telefones):
    for i in range(len(agenda_nomes)):
        print "Nome: %s" % agenda_nomes[i]
        print "Fone: %s" % agenda_telefones[i]
        print "----------"
        
while True:
    acao = raw_input()

    if acao == "inserir":
        quantidade = int(raw_input())
        inserir_contato(quantidade, agenda_nomes, agenda_telefones)
    elif acao == "buscar":
        nome = raw_input()
        buscar_contato(nome, agenda_nomes, agenda_telefones)
    elif acao == "imprimir":
        imprimir_agenda(agenda_nomes, agenda_telefones)
    elif acao == "finalizar": 
        break
