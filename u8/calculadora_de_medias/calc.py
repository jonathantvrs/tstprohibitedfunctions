# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

'''
Calcula Média Aritmética de números de uma lista
'''
def media_aritmetica(lista):
    soma_numeros, media_aritmetica = 0.0, 0.0
    for num in lista:
        soma_numeros += float(num)

    media_aritmetica = soma_numeros / len(lista)

    return media_aritmetica
'''
Calcula Média Geométrica de números de uma lista
'''
def media_geometrica(lista):
    multiplica_numeros, media_geometrica = 1.0, 0.0
    for num in lista:
        multiplica_numeros *= float(num)

    media_geometrica = multiplica_numeros ** (1.0 / len(lista))

    return media_geometrica
'''
Calcula Média Harmônica de números de uma lista
'''
def media_harmonica(lista):
    soma_inversos, media_harmonica = 0.0, 0.0
    for num in lista:
        soma_inversos += (1.0 / float(num))

    media_harmonica = len(lista) / soma_inversos

    return media_harmonica 

def calcula_media(lista_entradas, lista_numeros):
    for entrada in lista_entradas:
        if entrada == "MG":
            print "Média Geométrica: %.4f" % media_geometrica(lista_numeros)
        elif entrada == "MH":
            print "Média Harmônica: %.4f" % media_harmonica(lista_numeros)
        elif entrada == "MA":
            print "Média Aritmética: %.4f" % media_aritmetica(lista_numeros)
    print "----"


def main():
    while True:
        entrada = raw_input()
        if entrada == "Q":
            break
        numeros = raw_input()
        lista_entradas = entrada.split()
        lista_numeros = numeros.split()
    
        calcula_media(lista_entradas, lista_numeros)  

main()  
