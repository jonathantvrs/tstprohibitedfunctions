# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

binario = raw_input()
decimal, operacao = 0, 0

for i in range(len(binario)):
    operacao = int(binario[i]) * 2 ** (len(binario) - i - 1)
    print "%d * %d = %d" % (int(binario[i]), (2 ** (len(binario) - i - 1)), operacao)
    decimal += operacao 
print "%d(2) = %d(10)" % (int(binario), decimal)
