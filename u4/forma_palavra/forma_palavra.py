# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

first_word, second_word, third_word = raw_input(), raw_input(), raw_input()

formed_word = ""
words_size = len(first_word)
for i in range(words_size):
    if not first_word[i].isdigit():
        if first_word[i] > second_word[i] and first_word[i] > third_word[i]:
            formed_word += first_word[i]
        if first_word[i] == second_word[i] and first_word[i] == third_word[i]:
            formed_word += first_word[i]
    if not second_word[i].isdigit():
        if second_word[i] > first_word[i] and second_word[i] > third_word[i]:
            formed_word += second_word[i]
        if second_word[i] == first_word[i] and second_word[i] == third_word[i] and formed_word[i] != second_word[i]:
            formed_word += second_word[i]
    if not second_word[i].isdigit():
        if third_word[i] > first_word[i] and third_word[i] > second_word[i]:
            formed_word += third_word[i]

print formed_word
