# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_replace(string, parameter, new_parameter):
    string_aux = ""
    searched_string = ""

    for index in range(len(string)):
        if string[index].lower() == parameter[0].lower():
            for sec_index in range(len(parameter)):
                if string[index + sec_index].lower() == parameter[sec_index].lower():
                    searched_string += string[index + sec_index]
            if searched_string == parameter:
                string_aux += new_parameter

        else:
            string_aux += string[index]

    return string_aux

a = raw_input()

print a
print custom_replace(a, "I am", "We are")
