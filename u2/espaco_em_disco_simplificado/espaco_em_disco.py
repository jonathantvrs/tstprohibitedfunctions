# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

first_user = raw_input() 
first_space = int(raw_input()) 
second_user = raw_input()
second_space = int(raw_input())
third_user = raw_input()
third_space = int(raw_input())

occuped_space = (first_space + second_space + third_space) / (1024.0 * 1024.0)

print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado\n"
print "1, %s, %.2f MB" % (first_user, (first_space / (1024 * 1024.0))) 
print "2, %s, %.2f MB" % (second_user, (second_space / (1024 * 1024.0)))
print "3, %s, %.2f MB" % (third_user, (third_space / (1024 * 1024.0)))
print ""
print "Espaço total ocupado: %.2f MB" % occuped_space
print "Espaço médio ocupado: %.2f MB" % (occuped_space / 3)

