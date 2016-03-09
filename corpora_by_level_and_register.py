"""
Created on 07 March 2016
Updated on 09 March 2016
@author: pat
"""
from nltk.corpus import brown, nps_chat


news_easy = list()
for sentence in brown.tagged_sents(fileids="ca14"):
    news_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ca43"):
    news_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ca32"):
    news_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ca07"):
    news_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ca30"):
    news_easy.append(sentence)


news_advanced = list()
for sentence in brown.tagged_sents(fileids="ca42"):
    news_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ca18"):
    news_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ca24"):
    news_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ca08"):
    news_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ca11"):
    news_advanced.append(sentence)


news_difficult = list()
for sentence in brown.tagged_sents(fileids="ca35"):
    news_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ca05"):
    news_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ca36"):
    news_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ca04"):
    news_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ca44"):
    news_difficult.append(sentence)


editorial_easy = list()
for sentence in brown.tagged_sents(fileids="cb13"):
    editorial_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cb19"):
    editorial_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cb10"):
    editorial_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cb23"):
    editorial_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cb17"):
    editorial_easy.append(sentence)

# done
editorial_advanced = list()
for sentence in brown.tagged_sents(fileids="cb24"):
    editorial_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cb01"):
    editorial_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cb05"):
    editorial_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cb20"):
    editorial_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cb27"):
    editorial_advanced.append(sentence)


editorial_difficult = list()
for sentence in brown.tagged_sents(fileids="cb25"):
    editorial_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cb21"):
    editorial_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cb22"):
    editorial_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cb07"):
    editorial_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cb03"):
    editorial_difficult.append(sentence)


reviews_easy = list()
for sentence in brown.tagged_sents(fileids="cc15"):
    reviews_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cc07"):
    reviews_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cc01"):
    reviews_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cc03"):
    reviews_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="cc10"):
    reviews_easy.append(sentence)


reviews_advanced = list()
for sentence in brown.tagged_sents(fileids="cc05"):
    reviews_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cc04"):
    reviews_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cc13"):
    reviews_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cc02"):
    reviews_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="cc17"):
    reviews_advanced.append(sentence)


reviews_difficult = list()
for sentence in brown.tagged_sents(fileids="cc14"):
    reviews_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cc08"):
    reviews_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cc12"):
    reviews_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cc09"):
    reviews_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="cc06"):
    reviews_difficult.append(sentence)


government_easy = list()
for sentence in brown.tagged_sents(fileids="ch15"):
    government_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ch01"):
    government_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ch07"):
    government_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ch04"):
    government_easy.append(sentence)
for sentence in brown.tagged_sents(fileids="ch28"):
    government_easy.append(sentence)


government_advanced = list()
for sentence in brown.tagged_sents(fileids="ch14"):
    government_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ch06"):
    government_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ch30"):
    government_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ch20"):
    government_advanced.append(sentence)
for sentence in brown.tagged_sents(fileids="ch11"):
    government_advanced.append(sentence)


government_difficult = list()
for sentence in brown.tagged_sents(fileids="ch12"):
    government_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ch29"):
    government_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ch22"):
    government_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ch26"):
    government_difficult.append(sentence)
for sentence in brown.tagged_sents(fileids="ch23"):
    government_difficult.append(sentence)


chat_easy = list()
for post in nps_chat.tagged_posts(fileids="11-08-teens_706posts.xml"):
    chat_easy.append(post)
for post in nps_chat.tagged_posts(fileids="11-08-40s_706posts.xml"):
    chat_easy.append(post)
for post in nps_chat.tagged_posts(fileids="11-06-adults_706posts.xml"):
    chat_easy.append(post)
for post in nps_chat.tagged_posts(fileids="10-19-20s_706posts.xml"):
    chat_easy.append(post)
for post in nps_chat.tagged_posts(fileids="11-08-20s_705posts.xml"):
    chat_easy.append(post)


chat_advanced = list()
for post in nps_chat.tagged_posts(fileids="11-09-teens_706posts.xml"):
    chat_advanced.append(post)
for post in nps_chat.tagged_posts(fileids="11-09-adults_706posts.xml"):
    chat_advanced.append(post)
for post in nps_chat.tagged_posts(fileids="10-24-40s_706posts.xml"):
    chat_advanced.append(post)
for post in nps_chat.tagged_posts(fileids="10-19-40s_686posts.xml"):
    chat_advanced.append(post)
for post in nps_chat.tagged_posts(fileids="11-08-adults_705posts.xml"):
    chat_advanced.append(post)

chat_difficult = list()
for post in nps_chat.tagged_posts(fileids="10-19-30s_705posts.xml"):
    chat_difficult.append(post)
for post in nps_chat.tagged_posts(fileids="11-09-20s_706posts.xml"):
    chat_difficult.append(post)
for post in nps_chat.tagged_posts(fileids="11-09-40s_706posts.xml"):
    chat_difficult.append(post)
for post in nps_chat.tagged_posts(fileids="10-19-adults_706posts.xml"):
    chat_difficult.append(post)
for post in nps_chat.tagged_posts(fileids="10-26-teens_706posts.xml"):
    chat_difficult.append(post)
