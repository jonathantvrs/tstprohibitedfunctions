# coding: utf-8
# author: jonathan.tavares.silva
# matricula: 118210631

veiculo = raw_input()
pedagio = 0
frase_valor = "Valor a pagar: R$"

if veiculo == "Automóvel utilitário":
    pedagio = 11.40
    
    print "%s %.2f." % (frase_valor, pedagio)
elif veiculo == "Ônibus":
    eixos = int(raw_input())
    pedagio = eixos * 11.40
    
    print "%s %.2f." % (frase_valor, pedagio)
elif veiculo == "Caminhão":
    eixos = int(raw_input())
    pedagio = eixos * 9.60
    
    print "%s %.2f." % (frase_valor, pedagio)
elif veiculo == "Motocicleta":
    pedagio = 5.70

    print "%s %.2f." % (frase_valor, pedagio)
else:
    print "Veículo não cadastrado."
