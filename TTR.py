'''
Created on 20 Feb 2016
Updated on 24 Feb 2016

@author: kibs
'''
import nltk
import re
from nltk.corpus import brown 

def is_word(string):
    find_letter = re.search('[a-z]', string)
    return bool(find_letter)

# take a list of words
def TTR(text):
    tokens = 0.0
    type = 0.0
    word_list = list()
    for word in text:
        word = word.lower()
        if is_word(word):
            tokens += 1
        else:
            continue
        if word_list.__contains__(word):
            continue
        else:
            word_list.append(word)
            type += 1
    return type/tokens 

def TTR_tagged(tagged_text):
    tokens = 0.0
    type = 0.0
    word_list = list()
    for (word, tag) in tagged_text:
        word = word.lower()
        if is_word(word):
            tokens += 1
        else:
            continue
        if word_list.__contains__(word):
            continue
        else:
            word_list.append(word)
            type += 1
    return type/tokens

def TTR_tagged_sents(tagged_sents):
    tokens = 0.0
    type = 0.0
    word_list = list()
    for sent in tagged_sents:
        for (word, tag) in sent:
            word = word.lower()
            if is_word(word):
                tokens += 1
            else:
                continue
            if word_list.__contains__(word):
                continue
            else:
                word_list.append(word)
                type += 1
    return type/tokens

print 'TTR of list containing symbols: ' + str(TTR(['a','b','c','d','e','e','.','.']))

news_words = brown.words(fileids="ca16")
print 'TTR of list of news words:      ' + str(TTR(news_words))
news_tagged = brown.tagged_words(fileids="ca16")
print 'TTR of list of (word, tag):     ' + str(TTR_tagged(news_tagged))
news_tagged_sents = brown.tagged_sents(fileids='ca16')
print 'TTR of list of lists:           ' + str(TTR_tagged_sents(news_tagged_sents))
