# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

area_construida = float(raw_input())
valor_m2 = float(raw_input())
opcao_pagamento = raw_input()

iptu = area_construida * valor_m2

if opcao_pagamento == "vista":
    iptu -= iptu * 0.2
    print "Total: R$ %.2f" % iptu
elif opcao_pagamento == "2x":
    iptu -= iptu * 0.1
    print "Total: R$ %.2f. Parcelas: R$ %.2f" % (iptu, (iptu / 2))
elif opcao_pagamento == "3x":
    iptu -= iptu * 0.05
    print "Total: R$ %.2f. Parcelas: R$ %.2f" % (iptu, (iptu / 3))
