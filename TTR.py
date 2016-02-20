'''
Created on 20 Feb 2016
Updated on 21 Feb 2016

@author: kibs
'''

from corpustags import news_words, news_tagged

# take a list of words
def TTR(text):
    tokens = len(text)
    type = 0.0
    word_list = list()
    for word in text:
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
        if word_list.__contains__(word):
            continue
        else:
            word_list.append(word)
            type = type + 1.0
    return type/tokens

#print news_words
print TTR(news_words)

print TTR_tagged(news_tagged)
