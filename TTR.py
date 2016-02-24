'''
Created on 20 Feb 2016
Updated on 24 Feb 2016

@author: kibs
'''
import nltk
from nltk.corpus import brown 

# take a list of words
def TTR(text):
    tokens = len(text)
    type = 0.0
    word_list = list()
    for word in text:
        word = word.lower()
        if word_list.__contains__(word):
            continue
        else:
            word_list.append(word)
            type = type + 1.0
    return type/tokens 

def TTR_tagged(tagged_text):
    tokens = len(tagged_text)
    type = 0.0
    word_list = list()
    for (word, tag) in tagged_text:
        word = word.lower()
        if word_list.__contains__(word):
            continue
        else:
            word_list.append(word)
            type = type + 1.0
    return type/tokens

print TTR(['a','b','c','d','e','e'])

news_words = brown.words(fileids="ca16")
print TTR(news_words)
news_tagged = brown.tagged_words(fileids="ca16")
print TTR_tagged(news_tagged)
