def custom_count(list, parameter):
    counter = 0

    for element in list:
        if element == parameter:
            counter = counter + 1

    return counter

# assert custom_count(["abc", 2, 123, "abc", "qwe"], "abc") == 2
# assert custom_count([123, 234, "abc", 345], 123) == 1
# assert custom_count(["abc"], "abc") == 1
