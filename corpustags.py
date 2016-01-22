'''
Created on 22 Jan 2016

@author: kibs
'''

import nltk
from nltk.corpus import brown

# 1 ca16    news
# 2 cb02    editorial
# 3 cc17    reviews 

news_tagged_sents = brown.tagged_sents(fileids="ca16")
print "No. of news sentences = " + str(len(news_tagged_sents))

editorial_tagged_sents = brown.tagged_sents(fileids="cb02")
print "No. of editorial sentences = " + str(len(editorial_tagged_sents))

review_tagged_sents = brown.tagged_sents(fileids="cc17")
print "No. of review sentences = " + str(len(review_tagged_sents))

# to get the tags of x_tagged_sents
news_sent_1 = news_tagged_sents[0]

print news_sent_1
print "Length of sentence: " + str(len(news_sent_1))
for (word, tag) in news_sent_1:
    print tag

# news_sent_1 without the tags 
print brown.sents(fileids="ca16")[0]
