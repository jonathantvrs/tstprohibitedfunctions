# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

initial_space = float(raw_input("Posição inicial? "))
initial_velocity = float(raw_input("Velocidade inicial? "))
time = float(raw_input("Tempo? "))
aceleration = float(raw_input("Aceleração? "))

final_velocity = initial_velocity + aceleration * time
final_space = initial_space + initial_velocity * time + (aceleration * time ** 2) / 2
avg_velocity = initial_velocity + (aceleration * time) / 2 

print "\nDados da questão"
print "================"
print "   Posição inicial: %.2f m" % initial_space
print "Velocidade inicial: %.2f m/s" % initial_velocity
print "        Aceleração: %.2f m/s2" % aceleration
print "             Tempo: %.2f s" % time
print "  Velocidade final: %.2f m/s" % final_velocity
print "  Velocidade média: %.2f m/s" % avg_velocity
print "     Posição final: %.2f m" % final_space

