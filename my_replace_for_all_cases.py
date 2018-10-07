# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_replace(string, parameter, new_parameter):
    # variavel que recebe string com as trocas
    string_aux = ""
    # variavel que recebe string procurada (parameter)
    searched_string = ""
    # variavel de control do while
    index = 0

    # laço que vai executar ate a variavel de controle atingir o tamanho da string
    while index < len(string):
        # condição que testa se string na posicao index é igual a string procurada na posicao 0
        if string[index].lower() == parameter[0].lower():
            # laço para iterar sobre a palavra procurada
            for sec_index in range(len(parameter)):
                # condição que testa caracter a caracter da string com a procurada
                if string[index + sec_index].lower() == parameter[sec_index].lower():
                    # enquanto for igual, string procurada recebe string na posicao atual + a posicao do segundo for
                    searched_string += string[index + sec_index]
                else:
                    # se for diferente, a string é acumulada na nova string
                    string_aux += searched_string
            # condicao que testa se a string procurada formada é igual a que é para ser substituida
            if searched_string.lower() == parameter.lower():
                string_aux += new_parameter
                searched_string = ""
                index += len(parameter)
        else:
            string_aux += string[index]
            index += 1

    return string_aux

# assert custom_replace("Eu sou Jonathan. Me chamam de Jonathan. Mas prefiro Jon.", "Jonathan", "Wesley") == \
#                        "Eu sou Wesley. Me chamam de Wesley. Mas prefiro Jon."
# assert custom_replace("aaaaa", "a", "b") == "bbbbb"
# assert custom_replace("I am Jon. I am a boy", "I am", "We are") == "We are Jon. We are a boy"
