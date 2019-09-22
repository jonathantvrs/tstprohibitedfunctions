# -*- coding: utf-8 -*-
# jonathan.tavares.silva
# 118210631

def my_slice(p, l):
	digitos_periodo = ''
	for i in range(0, p):
		digitos_periodo += l[i]
		
	return digitos_periodo


def my_in(p, l):
	for e in l:
		if e == p:
			return True
	return False


def agrupa_por_periodo(turma):
	mapa_matricula = {}

	for i in range(len(turma)):
		periodo = my_slice(3, turma[i])
		if my_in(periodo, mapa_matricula):
			mapa_matricula[periodo] += 1
		else:
			mapa_matricula[periodo] = 1
	return mapa_matricula

print agrupa_por_periodo(['0111', '0112', '0221', '0222'])
