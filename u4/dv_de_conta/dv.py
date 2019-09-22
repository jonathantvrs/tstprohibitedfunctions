# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

bank_account = raw_input()

sum_digits = 0
for i in range(len(bank_account)):
    sum_digits += int(bank_account[i])

verify_digit = str(sum_digits % 11)

if verify_digit == "10":
    verify_digit = "X"

print "%s-%s" % (bank_account, verify_digit)
