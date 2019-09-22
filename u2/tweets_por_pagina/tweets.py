# -*- coding: utf-8 -*-
# author: jonathan.tavares.silva
# matricula: 118210631

quantidade_tweets = int(raw_input())

paginas_necessarias = quantidade_tweets / 400
tweets_perdidos = quantidade_tweets % 400
porcentagem_perdidos = tweets_perdidos / float(quantidade_tweets) * 100.0  

print "Serão necessárias %d página(s) para visualizar os tweets." % paginas_necessarias
print "%.1f%% dos tweets serão perdidos." % porcentagem_perdidos
