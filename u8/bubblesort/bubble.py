# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def bubblesort(dados):
    for i in range(len(dados) - 1):
        for j in range(len(dados) - 1):
            if dados[j] > dados[j + 1]:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]
