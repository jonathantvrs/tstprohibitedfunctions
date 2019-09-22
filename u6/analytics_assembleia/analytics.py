# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def custom_split(lista, parametro):
    new_list = []
    string_aux = ""

    for elemento in lista:
        if elemento != parametro:
            string_aux += elemento
        else:
            new_list.append(string_aux)
            string_aux = ""
    if string_aux != "" or string_aux != parametro:
        new_list.append(string_aux)
    
    return new_list
            
    
def conta_votos(votacoes, id_votacao):
    lista_votos = []
    conta_sim, conta_nao = 0, 0

    for i in range(len(votacoes)):
        string = custom_split(votacoes[i], ",")
        
        for i in range(len(string)):
            if string[i] == str(id_votacao):
                if string[i - 1] == "sim":
                    conta_sim += 1
                else:
                    conta_nao += 1
    lista_votos = [conta_sim, conta_nao]
 
    return lista_votos

votacao = []
votacao.append('greve geral,sim,543,joao,servidor')
votacao.append('greve geral,nao,543,marina,servidor')

#print conta_votos(votacao, 543)
