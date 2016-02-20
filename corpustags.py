'''
Created on 22 Jan 2016
Updated on 20 Feb 2016

@author: kibs
'''

import nltk
from nltk.corpus import brown

# 1 ca16    news
# 2 cb02    editorial
# 3 cc17    reviews 

news_words = brown.words(fileids="ca16")
news_tagged = nltk.pos_tag(news_words)
print news_tagged

'''
news_sents = brown.sents(fileids="ca16")
print nltk.pos_tag(news_sents)
ERROR
nltk.pos_tag() takes list of words
news_sents is a list of list of words/list of sentences
'''

news_tagged_sents = brown.tagged_sents(fileids="ca16")
print news_tagged_sents
print "No. of news sentences = " + str(len(news_tagged_sents))

editorial_tagged_sents = brown.tagged_sents(fileids="cb02")
print "No. of editorial sentences = " + str(len(editorial_tagged_sents))

review_tagged_sents = brown.tagged_sents(fileids="cc17")
print "No. of review sentences = " + str(len(review_tagged_sents))

# to get the tags of x_tagged_sents
news_sent_1 = news_tagged_sents[20]

print news_sent_1
print "Length of sentence: " + str(len(news_sent_1))
for (word, tag) in news_sent_1:
    print tag

# news_sent_1 without the tags 
print brown.sents(fileids="ca16")[20]

count = 0
for sent in news_tagged_sents:
    for (word, tag) in sent:
        if tag[:2]=="NP":
            count = count + 1

print str(count)
