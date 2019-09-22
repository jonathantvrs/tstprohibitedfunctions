# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

quantidade_de_morangos = int(raw_input())

quantidade_de_caixas = quantidade_de_morangos / 400
porcentagem_de_morangos_perdidos = quantidade_de_morangos % 400.0 * 100 / quantidade_de_morangos

print "Serão necessárias %d caixa(s) para embalar os morangos." % quantidade_de_caixas
print "%.1f%% dos morangos serão perdidos." % porcentagem_de_morangos_perdidos
