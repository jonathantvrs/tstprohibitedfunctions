# coding:utf-8
# jonathan.tavares.silva
# 118210631

def busca_matriz(m, e):
	lista_posicoes = []
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == e:
				lista_posicoes.append((i,j))
	return lista_posicoes
				
	
