# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_in(list, parameter):
    for element in list:
        if element == parameter:
            return True
        return False

# assert custom_in(["a", "oam", "okay"],"b") == False
# assert custom_in(["b", "aom", "okay"]) == True
