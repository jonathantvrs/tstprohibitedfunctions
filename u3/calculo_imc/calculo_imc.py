# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

peso = float(raw_input())
altura = float(raw_input())

imc = peso / (altura ** 2)

if imc < 16:
    classificacao = 'Magreza grave'
elif 16 <= imc < 17:
    classificacao = 'Magreza moderada'
elif 17 <= imc < 18.5:
    classificacao = 'Magreza leve'
elif 18.5 <= imc < 25:
    classificacao = 'Saudável'
elif 25 <= imc < 30:
    classificacao = 'Sobrepeso'
elif 30 <= imc < 35:
    classificacao = 'Obesidade Grau I'
elif 35 <= imc < 40:
    classificacao = 'Obesidade Grau II (severa)'
else:
    classificacao = 'Obesidade Grau III (mórbida)'

print "IMC: %.1f - %s" % (imc, classificacao)
