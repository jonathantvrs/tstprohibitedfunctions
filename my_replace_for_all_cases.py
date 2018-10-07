# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_replace(string, parameter, new_parameter):
    string_aux = ""
    searched_string = ""
    index = 0

    while index < len(string):
        if string[index].lower() == parameter[0].lower():
            for sec_index in range(len(parameter)):
                if string[index + sec_index].lower() == parameter[sec_index].lower():
                    searched_string += string[index + sec_index]
                else:
                    string_aux += searched_string
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
