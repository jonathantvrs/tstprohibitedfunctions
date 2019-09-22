# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

num_investiments = 0.0
sum_investiments, average_investiments = 0.0, 0.0
while True:
    investiment = float(raw_input())
    num_investiments += 1.0
    
    if investiment >= average_investiments:
        
        sum_investiments += investiment
    else:
        break
    average_investiments = sum_investiments / num_investiments
    
   
print "Saldo total do FIS: R$%.2f." % sum_investiments
print "Média das contribuições: R$%.2f." % average_investiments
        

