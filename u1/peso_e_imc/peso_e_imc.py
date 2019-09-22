# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

peso = float(raw_input())
altura = float(raw_input())

imc = peso / altura ** 2
peso_ganhar_ou_perder = (24.9 - imc) * altura ** 2 

print "IMC atual = %.2f" % imc
print "Peso a ser ganho/perdido = %.2f" % peso_ganhar_ou_perder 
