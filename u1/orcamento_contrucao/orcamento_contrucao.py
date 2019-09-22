# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

preco_unidade_tijolo = float(raw_input("Digite o preço da unidade do tijolo (Em reais): "))
altura_tijolo = float(raw_input("Digite a altura do tijolo (Em metros): "))
comprimento_tijolo = float(raw_input("Digite o comprimento do tijolo (Em metros): "))
altura_paredes = float(raw_input("Digite a altura das paredes (Em metros): "))
comprimento_paredes = float(raw_input("Digite o comprimento das paredes (Em metros): "))

qtd_tijolos_altura = altura_paredes / altura_tijolo
qtd_tijolos_largura = comprimento_paredes / comprimento_tijolo
qtd_tijolos_total = qtd_tijolos_altura * qtd_tijolos_largura

preco_final_tijolos = qtd_tijolos_total * preco_unidade_tijolo

print "O número total de tijolos é %.1f e o orçamento final é de R$ %.1f" % (qtd_tijolos_total, preco_final_tijolos)
