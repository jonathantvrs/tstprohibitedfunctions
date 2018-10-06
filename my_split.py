# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_split(string, separator):
    elements = []
    string_aux = ""

    for element in string:
        if element != separator:
            string_aux += element
        else:
            elements.append(string_aux)
            string_aux = ""
    if string_aux != "" or string_aux != separator:
        elements.append(string_aux)
    return elements

# print custom_split("Jonathan Everton Wesley", " ")

# assert custom_split("Jonathan,Everton", ",") == ['Jonathan', 'Everton']
