"""
Created on 21 Feb 2016
@author: pat & anki
"""

from corpustags import news_tagged_sents, editorial_tagged_sents, review_tagged_sents
from nps_tags import nps_chat_tagged


def sentence_length(tagged_corpus):
    sent_and_length=list()
    num_of_iter=0
    for sent in tagged_corpus:
        sent_length=0
        for (word,tag) in sent:
            sent_length+=1
        sent_and_length.append((num_of_iter, sent_length))
        num_of_iter+=1
    return sent_and_length


def single_sent_length(sentence):
    sentence_length=0
    for (word,tag) in sentence:
        sentence_length+=1
    return sentence_length


def num_of_sents(tagged_corpus):
    sent_count=0
    for sent in tagged_corpus:
        sent_count+=1
    return sent_count


def average_sent_length(tagged_corpus):
    total_length=0
    sent_count=0
    average_length=0
    for sent in tagged_corpus:
        sent_count+=1.0
        sent_length=0
        for (word,tag) in sent:
            sent_length+=1.0
        total_length = total_length+sent_length
    average_length = total_length/sent_count
    return average_length


# Test sentence length for text from Brown corpus
print "Sentence analysis of Brown EDITORIAL corpus"
for item in sentence_length(editorial_tagged_sents):
    print "Sentence No. (" + str(item[0]) + ") and its length <" + str(item[1]) + ">"

print "Total number of sentences in Brown editorial corpus: "+ str(num_of_sents(editorial_tagged_sents))


# Test sentence length for chat corpus
print "Sentence analysis of CHAT corpus"
for item in sentence_length(nps_chat_tagged):
    print "Sentence No. (" + str(item[0]) + ") and its length <" + str(item[1]) + ">"

print "Total number of sentences in chat corpus: "+ str(num_of_sents(nps_chat_tagged))


# Test sentence length for random sentence
sentence = [("Who","WPO"), ("do","DO"), ("you","PPSS"), ("love","VB"), ("?",".")]
print "Length of a single sentence: " + str(single_sent_length(sentence))


# Test average sentence length for all corpora
print "Average sentence length of chat corpus: " + str(average_sent_length(nps_chat_tagged))
print "Average sentence length of news corpus: " + str(average_sent_length(news_tagged_sents))
print "Average sentence length of editorial corpus: " + str(average_sent_length(editorial_tagged_sents))
print "Average sentence length of review corpus: " + str(average_sent_length(review_tagged_sents))
