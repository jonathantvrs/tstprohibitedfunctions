# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

initial_space = float(raw_input())
velocity = float(raw_input())
time = float(raw_input())

space_in_function_of_time = initial_space + velocity * time

print "%.2f" % space_in_function_of_time
