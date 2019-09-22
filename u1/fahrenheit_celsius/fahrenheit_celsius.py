# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva@ccc.ufcg.edu.br
# matricula: 118210631

fahrenheit = float(raw_input())
celsius = (fahrenheit - 32) * 5 / 9 
kelvin = celsius + 273.15

print "Fahrenheit: %.3f F\nCelsius: %.3f C\nKelvin: %.3f K" % (fahrenheit, celsius, kelvin)
