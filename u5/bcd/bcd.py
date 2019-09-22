# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

bcd = raw_input()

while bcd != "fim":
    if len(bcd) == 8:
        first_binary = int(bcd[0] + bcd[1] + bcd[2] + bcd[3], 2)
        second_binary = int(bcd[4] + bcd[5] + bcd[6] + bcd[7], 2)
    
        if first_binary < 10 and second_binary < 10:
            print str(first_binary) + str(second_binary)
        else:
            print "BCD inválido."
    else: print "Tente novamente."

    bcd = raw_input()
        
