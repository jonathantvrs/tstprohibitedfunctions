# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

LETRAS_SENHA_FORTE = ['o', 'i', 'l', 'e', 'a', 'b', 't']
NUMEROS_SENHA_FORTE = ['0', '1', '1', '3', '4', '6', '7']

def my_in(p, l):
    for e in l:
        if e == p:
            return True
    return False

def retornaIndicePrimeiraOcorrencia(p, l):
    for i in range(len(l)):
        if l[i] == p:
            return i

def criaSenhaFraca(palavra):
    print "((" + palavra + "))"


def criaSenhaForte(palavra):
    senha_forte = ""

    for c in palavra:
        if my_in(c.lower(), LETRAS_SENHA_FORTE):
            indice_letra = retornaIndicePrimeiraOcorrencia(c.lower(), LETRAS_SENHA_FORTE)
            senha_forte += NUMEROS_SENHA_FORTE[indice_letra]
        else:
            senha_forte += c

    print "((" + senha_forte + "))"

def main():
    while True:
        entrada = raw_input()

        if entrada == "***":
            break
        else:
            entrada = entrada.split()
            senha = entrada[0]
            forca_senha = entrada[1]

            if forca_senha == "fraco":
                criaSenhaFraca(senha)
            elif forca_senha == "forte":
                criaSenhaForte(senha)

main()
