# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

# transforma decimal em binario de 8 bits
def dec_to_bin(numero):
    string_binario = bin(numero)

    novo_binario = ""
    
    if numero < 0:
        for i in range(3, len(string_binario)):
            novo_binario += string_binario[i]
    else:
        for i in range(2, len(string_binario)):
            novo_binario += string_binario[i]
    
    if len(novo_binario) < 8:
        diferenca = "0" * (8 - len(novo_binario))
        binario_com_8 = diferenca + novo_binario
        
        return binario_com_8      

    return novo_binario
            
# calcula binario em excesso de 127
def excesso_127(numero):
    print dec_to_bin(numero)
# calcula complemento de 1 de um numero decimal
def complemento1(numero):
    if numero < 0:
        numero = dec_to_bin(numero)

        novo_numero = ""
        for binario in numero:
            if binario == "0":
                novo_numero += "1"
            elif binario == "1":
                novo_numero += "0"
        print novo_numero      
    elif numero >= 0:
        print dec_to_bin(numero)

while True:
    entrada = raw_input()
    entrada = entrada.split()

    if entrada[0] == "***":
        break
    elif entrada[0] == "C1":
        complemento1(int(entrada[1]))
    elif entrada[0] == "E127":
        excesso_127(127 + int(entrada[1]))

