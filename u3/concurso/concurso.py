# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

escrita_um = float(raw_input())
didatica_um = float(raw_input())
titulacao_um = float(raw_input())
idade_um = int(raw_input())
escrita_dois = float(raw_input())
didatica_dois = float(raw_input())
titulacao_dois = float(raw_input())
idade_dois = int(raw_input())

media_um = (escrita_um * 0.3 + didatica_um * 0.4 + titulacao_um * 0.3) / 1.0
media_dois = (escrita_dois * 0.3 + didatica_dois * 0.4 + titulacao_dois * 0.3) / 1.0

if media_um == media_dois and idade_um == idade_dois:
    print "Empate."
else:
    if media_um > media_dois:
        print "O primeiro candidato foi aprovado com média %.1f." % media_um
    elif media_um < media_dois:
        print "O segundo candidato foi aprovado com média %.1f." % media_dois
    elif media_um == media_dois and idade_um > idade_dois:
        print "O primeiro candidato foi aprovado com média %.1f." % media_um
    elif media_um == media_dois and idade_um < idade_dois:
        print "O segundo candidato foi aprovado com média %.1f." % media_dois
