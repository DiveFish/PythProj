"""
Created on 07 March 2016
@author: Pat
"""
from nltk.corpus import brown

from nps_tags import nps_chat_tagged


news_easy = list()
for sentence in brown.sents(fileids="ca14"):
    news_easy.append(sentence)
for sentence in brown.sents(fileids="ca43"):
    news_easy.append(sentence)
for sentence in brown.sents(fileids="ca32"):
    news_easy.append(sentence)
for sentence in brown.sents(fileids="ca30"):
    news_easy.append(sentence)
for sentence in brown.sents(fileids="ca39"):
    news_easy.append(sentence)


news_advanced = list()
for sentence in brown.sents(fileids="ca25"):
    news_advanced.append(sentence)
for sentence in brown.sents(fileids="ca18"):
    news_advanced.append(sentence)
for sentence in brown.sents(fileids="ca22"):
    news_advanced.append(sentence)
for sentence in brown.sents(fileids="ca12"):
    news_advanced.append(sentence)
for sentence in brown.sents(fileids="ca13"):
    news_advanced.append(sentence)


news_difficult = list()
for sentence in brown.sents(fileids="ca35"):
    news_difficult.append(sentence)
for sentence in brown.sents(fileids="ca05"):
    news_difficult.append(sentence)
for sentence in brown.sents(fileids="ca36"):
    news_difficult.append(sentence)
for sentence in brown.sents(fileids="ca04"):
    news_difficult.append(sentence)
for sentence in brown.sents(fileids="ca44"):
    news_difficult.append(sentence)


editorial_easy = list()
for sentence in brown.sents(fileids="cb13"):
    editorial_easy.append(sentence)
for sentence in brown.sents(fileids="cb19"):
    editorial_easy.append(sentence)
for sentence in brown.sents(fileids="cb10"):
    editorial_easy.append(sentence)
for sentence in brown.sents(fileids="cb23"):
    editorial_easy.append(sentence)
for sentence in brown.sents(fileids="cb17"):
    editorial_easy.append(sentence)


editorial_advanced = list()
for sentence in brown.sents(fileids="cb24"):
    editorial_advanced.append(sentence)
for sentence in brown.sents(fileids="cb01"):
    editorial_advanced.append(sentence)
for sentence in brown.sents(fileids="cb12"):
    editorial_advanced.append(sentence)
for sentence in brown.sents(fileids="cb15"):
    editorial_advanced.append(sentence)
for sentence in brown.sents(fileids="cb06"):
    editorial_advanced.append(sentence)


editorial_difficult = list()
for sentence in brown.sents(fileids="cb25"):
    editorial_difficult.append(sentence)
for sentence in brown.sents(fileids="cb21"):
    editorial_difficult.append(sentence)
for sentence in brown.sents(fileids="cb22"):
    editorial_difficult.append(sentence)
for sentence in brown.sents(fileids="cb07"):
    editorial_difficult.append(sentence)
for sentence in brown.sents(fileids="cb02"):
    editorial_difficult.append(sentence)


reviews_easy = list()
for sentence in brown.sents(fileids="cc15"):
    reviews_easy.append(sentence)
for sentence in brown.sents(fileids="cc07"):
    reviews_easy.append(sentence)
for sentence in brown.sents(fileids="cc01"):
    reviews_easy.append(sentence)
for sentence in brown.sents(fileids="cc03"):
    reviews_easy.append(sentence)
for sentence in brown.sents(fileids="cc10"):
    reviews_easy.append(sentence)


reviews_advanced = list()
for sentence in brown.sents(fileids="cc16"):
    reviews_advanced.append(sentence)
for sentence in brown.sents(fileids="cc04"):
    reviews_advanced.append(sentence)
for sentence in brown.sents(fileids="cc11"):
    reviews_advanced.append(sentence)
for sentence in brown.sents(fileids="cc02"):
    reviews_advanced.append(sentence)
for sentence in brown.sents(fileids="cc17"):
    reviews_advanced.append(sentence)


reviews_difficult = list()
for sentence in brown.sents(fileids="cc14"):
    reviews_difficult.append(sentence)
for sentence in brown.sents(fileids="cc08"):
    reviews_difficult.append(sentence)
for sentence in brown.sents(fileids="cc12"):
    reviews_difficult.append(sentence)
for sentence in brown.sents(fileids="cc09"):
    reviews_difficult.append(sentence)
for sentence in brown.sents(fileids="cc06"):
    reviews_difficult.append(sentence)


government_easy = list()
for sentence in brown.sents(fileids="ch15"):
    government_easy.append(sentence)
for sentence in brown.sents(fileids="ch01"):
    government_easy.append(sentence)
for sentence in brown.sents(fileids="ch07"):
    government_easy.append(sentence)
for sentence in brown.sents(fileids="ch24"):
    government_easy.append(sentence)
for sentence in brown.sents(fileids="ch04"):
    government_easy.append(sentence)


government_advanced = list()
for sentence in brown.sents(fileids="ch14"):
    government_advanced.append(sentence)
for sentence in brown.sents(fileids="ch13"):
    government_advanced.append(sentence)
for sentence in brown.sents(fileids="ch10"):
    government_advanced.append(sentence)
for sentence in brown.sents(fileids="ch20"):
    government_advanced.append(sentence)
for sentence in brown.sents(fileids="ch11"):
    government_advanced.append(sentence)


government_difficult = list()
for sentence in brown.sents(fileids="ch12"):
    government_difficult.append(sentence)
for sentence in brown.sents(fileids="ch29"):
    government_difficult.append(sentence)
for sentence in brown.sents(fileids="ch22"):
    government_difficult.append(sentence)
for sentence in brown.sents(fileids="ch26"):
    government_difficult.append(sentence)
for sentence in brown.sents(fileids="ch23"):
    government_difficult.append(sentence)


chat_easy = list()
for sentence in nps_chat_tagged:
    chat_easy.append(sentence)

chat_advanced = list()
for sentence in nps_chat_tagged:
    chat_advanced.append(sentence)

chat_difficult = list()
for sentence in nps_chat_tagged:
    chat_difficult.append(sentence)
