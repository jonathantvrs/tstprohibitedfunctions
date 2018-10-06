# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_replace(string, parameter, new_parameter):
    string_aux = ""

    for element in string:
        if element.lower() == parameter.lower():
            string_aux += new_parameter
        else:
            string_aux += element

    return string_aux


test = raw_input()

print custom_replace(test, ",", " ")

# assert custom_replace("Rafael é feio", "a", "o") == "Rofoel é feio"
