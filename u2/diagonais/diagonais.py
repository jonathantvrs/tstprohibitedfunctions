# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

def diagonais(M):

    diagonal_principal = []
    diagonal_secundaria = []

    for i in range(len(M)):
        diagonal_principal.append(M[i][i])
        diagonal_secundaria.append(M[i][len(M) - 1 - i])
    return [diagonal_principal, diagonal_secundaria]
