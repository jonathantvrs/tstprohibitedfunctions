# coding: utf-8
# jonathan.tavares.silva
# 118210631	

def calcula_conta(tabela):
	tabela_valores = []
	for i in range(1, len(tabela)):
		for j in range(1, len(tabela[i])):
			tabela_valores.append(tabela[i][j])
	conta = 0.0
	for k in range(0, len(tabela_valores), 3):
		conta += tabela_valores[k] * tabela_valores[k + 1] * (float(tabela_valores[k + 2]) / 1000)
	
	return "R$ %.2f" % (conta * 0.28)

print calcula_conta([["Eqp", "Qtd", "Tmp", "Pot"],["Ar", 1,240,2000],["Pc", 2, 150, 180],["Tv", 3, 150, 110]])
