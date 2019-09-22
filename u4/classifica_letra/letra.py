# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

palavra = raw_input()

for caractere in palavra:
    if caractere in "aeiouAEIOU":
        print "<" + caractere + ">" + " " + "sim"
    else:
        print "<" + caractere + ">" + " " + "nao"
