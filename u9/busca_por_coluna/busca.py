# coding: utf-8
# jonathan.tavares.silva
# 118210631

def busca_todos_por_coluna_em_matriz(m, e):
	lista_posicoes_elemento = []

	for j in range(5):
		for i in range(len(m)):
			if m[i][j] == e:
				lista_posicoes_elemento.append((i,j))
					
	return lista_posicoes_elemento

print busca_todos_por_coluna_em_matriz([[2,3,5,3,1],[3,2,1,5,6],[3,2,3,2,1]], 3)

