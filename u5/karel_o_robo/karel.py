# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

c_x, c_y = 0, 0
while True:
    comando = raw_input()
    
    if comando[2] == "0":
        print "Fim de jogo"
        break
    else:
        if comando[0] == "C":
            c_y += int(comando[2])
        elif comando[0] == "B":
            c_y -= int(comando[2]) 
        elif comando[0] == "E":
            c_x -= int(comando[2]) 
        elif comando[0] == "D":
            c_x += int(comando[2]) 
    
        if abs(c_y) == (2 * abs(c_x)) and c_x != 0:
            print "Parabéns, conquista do portal (%d, %d)" % (c_x, c_y)
            break
