# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

custo_entrada = float(raw_input())
percentual_despesas = float(raw_input())
percentual_lucro = float(raw_input())
percentual_impostos = float(raw_input())
percentual_comissoes = float(raw_input())
percentual_descontos = float(raw_input())
percentual_encargos = float(raw_input())

preco_venda = ((custo_entrada + (custo_entrada * percentual_despesas / 100) + (custo_entrada * percentual_lucro / 100)) * 100.0) / (100.0 - percentual_impostos - percentual_comissoes - percentual_descontos - percentual_encargos)

preco_inteiro = int(preco_venda) / 1
preco_decimal = preco_venda % 1

print "Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" % (preco_venda, preco_inteiro, preco_decimal)


