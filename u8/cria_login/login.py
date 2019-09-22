# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def my_in(p, l):
    for e in l:
        if e == p:
            return True
    return False
    
def my_split(seq, p):
    els = []
    str_aux = ""

    for el in seq:
        if el != p:
            str_aux += el
        else:
            els.append(str_aux)
            str_aux = ""
    if str_aux != "" or str_aux != p:
        els.append(str_aux)
    
    return els

def cria_login(nome):
    lista_nome = my_split(nome, " ")
    login = ""    

    for i in range(len(lista_nome)):
        nome = lista_nome[i]
        if i == 0:
            for l in nome:
                login += l.lower()
        else:
            if not my_in(nome[0] + nome[1], ["da", "de", "di", "do", "du"]):
                login += nome[0].lower()
    return login


while True:
    nome = raw_input()
    
    if nome != "fim":
        print "%s: %s" % (nome, cria_login(nome))
    else:
        break
    
