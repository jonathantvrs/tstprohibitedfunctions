# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

saldo, gasto, maior, mes = 0, 0, -99999, 0

for i in range(12):
    gasto = int(raw_input())
    saldo += 500 - gasto 
 
    if saldo > maior:
        maior = saldo
        mes = i + 1
    elif saldo == maior:
        maior = saldo
        mes = i + 1

if mes == 1: print "jan"
elif mes == 2: print "fev"
elif mes == 3: print "mar"
elif mes == 4: print "abr"
elif mes == 5: print "mai"
elif mes == 6: print "jun"
elif mes == 7: print "jul"
elif mes == 8: print "ago"
elif mes == 9: print "set"
elif mes == 10: print "out"
elif mes == 11: print "nov"
else: print "dez" 


