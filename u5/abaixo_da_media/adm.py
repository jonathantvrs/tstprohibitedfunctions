# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

value = raw_input()

iterator, avg_values, sum_values = 0, 0, 0
accumulator = []
while value != "fim":
    iterator += 1.0
    accumulator.append(value)
    sum_values += int(value)

    value = raw_input()

avg_values = sum_values / iterator

print "%.2f" % avg_values

for i in range(len(accumulator)):
    if int(accumulator[i]) < avg_values:
        print str(i+1) + " " + accumulator[i]
