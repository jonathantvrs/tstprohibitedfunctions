# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

brinquedos_vendidos = int(raw_input())
vendidos_teresa = int(raw_input())
vendidos_carla = int(raw_input())

vendidos_joaquim = brinquedos_vendidos - (vendidos_teresa + vendidos_carla)
porcentagem_teresa = vendidos_teresa / float(brinquedos_vendidos) * 100
porcentagem_carla = vendidos_carla / float(brinquedos_vendidos) * 100
porcentagem_joaquim = vendidos_joaquim / float(brinquedos_vendidos) * 100

print "Teresa vendeu %d (de %d) brinquedos. (%.2f%%)" % (vendidos_teresa, brinquedos_vendidos, porcentagem_teresa)
print "Joaquim vendeu %d (de %d) brinquedos. (%.2f%%)" % (vendidos_joaquim, brinquedos_vendidos, porcentagem_joaquim)
print "Carla vendeu %d (de %d) brinquedos. (%.2f%%)" % (vendidos_carla, brinquedos_vendidos, porcentagem_carla)
