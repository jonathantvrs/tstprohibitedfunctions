# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631


def busca_matriz(m, e):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == e:
                return (i,j)
    return None


print busca_matriz([[],[2],[]], 1)
print busca_matriz([[2,3,5,3,1],[3,2,1,5,6],[1,2,3,2,1]], 3)
print busca_matriz([[2,3,5,3],[3,2,1,5,6],[1,2,3,2,1]], 1)
print busca_matriz([[2,3,5,3,1],[3,2,1,5,6],[1,2,3,2,1]], 3)
print busca_matriz([[2,3,5,3,1],[3,2,1,5,6],[1,2,3,2,1]], 4)
