# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631
import math

first_sequence = raw_input().split()
second_sequence = raw_input().split()

first_sum = 0
for i in range(len(first_sequence)):
    first_sum += float(first_sequence[i])

second_sum = 0
for j in range(len(second_sequence)):
    second_sum += float(second_sequence[j])

first_avg = first_sum / len(first_sequence)
second_avg = second_sum / len(second_sequence)

desvio_first = 0
for k in range(len(first_sequence)):
    desvio_first += (float(first_sequence[k]) - first_avg) ** 2

desvio_second = 0
for m in range(len(second_sequence)):
    desvio_second += (float(second_sequence[m]) - second_avg) ** 2

desvio_first = math.sqrt(desvio_first / (len(first_sequence) - 1))
desvio_second = math.sqrt(desvio_second / (len(second_sequence) - 1))

if desvio_first > desvio_second:
    print "A sequência 1 possui o maior desvio padrão (%.2f)." % desvio_first
elif desvio_first == desvio_second:
    print "As sequências possuem o mesmo desvio padrão (%.2f)." % desvio_first
else:
    print "A sequência 2 possui o maior desvio padrão (%.2f)." % desvio_second
