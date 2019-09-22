# coding:utf-8
# jonathan.tavares.silva
# 118210631

def coluna(m, index):
	coluna_matriz = []
	for i in range(len(m)):
		coluna_matriz.append(m[i][index])
	
	return coluna_matriz
