# -*- coding: utf-8 -*-
# jonathan.tavares.silva
# 118210631

def agrupa_negativos(l):
	negativos_positivos = {'nao-negativos': [], 'negativos': []}

	for i in range(len(l)):
		if l[i] >= 0:
			negativos_positivos['nao-negativos'].append(l[i])
		else:
			negativos_positivos['negativos'].append(l[i])
	return negativos_positivos

print agrupa_negativos([])
print agrupa_negativos([1,-2,0,1])
print agrupa_negativos([-2222, -1, -6])
print agrupa_negativos([222, 1, 0, 3, 4])
