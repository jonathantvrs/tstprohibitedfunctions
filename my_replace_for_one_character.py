# -*-  coding: utf-8  -*-
# author: jonathantvrs

def custom_replace(sequence, parameter, new_parameter):
	new_sequence = ''
	for element in sequence:
		if element == parameter: new_sequence += new_parameter 
		else: new_sequence += element
	
	return new_sequence

assert custom_replace("Rafael é feio", "a", "o") == "Rofoel é feio"
