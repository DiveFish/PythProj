"""
Created on 21 Feb 2016
@author: Pat
"""

from corpustags import news_tagged_sents, editorial_tagged_sents, review_tagged_sents
from nps_tags import nps_chat_tagged
from tag_set import penn_punct, brown_punct


def sentence_length_corpus(tagged_corpus):
    sent_and_length=list()
    num_of_iter = 0
    for sent in tagged_corpus:
        sent_length = 0
        for (word, tag) in sent:
            sent_length += 1
        sent_and_length.append((num_of_iter, sent_length))
        num_of_iter += 1
    return sent_and_length


def single_sent_length(sent):
    sent_length = 0
    for (word, tag) in sent:
        sent_length += 1
    return sent_length


def num_of_sent(tagged_corpus):
    sent_count = 0
    for sent in tagged_corpus:
        sent_count += 1
    return sent_count


def single_sent_word_length(sentence):
    total_num_of_letters = 0
    word_count = 0
    for (word, tag) in sentence:
        if not (penn_punct.__contains__(tag) or brown_punct.__contains__(tag)):
            word_count += 1.0
            for letter in word:
                total_num_of_letters+=1.0
    average_word_length = total_num_of_letters/word_count
    return average_word_length


def word_length_average(tagged_corpus):
    total_num_of_letters = 0
    word_count = 0
    for sent in tagged_corpus:
        for (word, tag) in sent:
            if not (penn_punct.__contains__(tag) or brown_punct.__contains__(tag)):
                word_count += 1.0
                for letter in word:
                    total_num_of_letters+=1.0
    average_word_length = total_num_of_letters/word_count
    return average_word_length


def sent_length_average(tagged_corpus):
    total_length = 0
    sent_count = 0
    for sent in tagged_corpus:
        sent_count += 1.0
        sent_length = 0
        for (word, tag) in sent:
            sent_length += 1.0
        total_length = total_length+sent_length
    average_sentence_length = total_length/sent_count
    return average_sentence_length


# Test sentence length for text from Brown corpus
print "Sentence analysis of Brown EDITORIAL corpus"
for item in sentence_length_corpus(editorial_tagged_sents):
    print "Sentence No. (" + str(item[0]) + ") and its length <" + str(item[1]) + ">"

print "Total number of sentences in Brown editorial corpus: "+ str(num_of_sent(editorial_tagged_sents))


# Test sentence length for chat corpus
print "Sentence analysis of CHAT corpus"
for item in sentence_length_corpus(nps_chat_tagged):
    print "Sentence No. (" + str(item[0]) + ") and its length <" + str(item[1]) + ">"

print "Total number of sentences in chat corpus: "+ str(num_of_sent(nps_chat_tagged))


# Test sentence length for random sentence
sentence = [("Who","WPO"), ("do","DO"), ("you","PPSS"), ("love","VB"), ("?",".")]
print "Length of a single sentence: " + str(single_sent_length(sentence))


# Test average sentence length for all corpora
print "Average sentence length of chat corpus: " + str(sent_length_average(nps_chat_tagged))
print "Average sentence length of news corpus: " + str(sent_length_average(news_tagged_sents))
print "Average sentence length of editorial corpus: " + str(sent_length_average(editorial_tagged_sents))
print "Average sentence length of review corpus: " + str(sent_length_average(review_tagged_sents))

print "\n"
print "Average word length of chat corpus: " + str(word_length_average(nps_chat_tagged))
print "Average word length of news corpus: " + str(word_length_average(news_tagged_sents))
print "Average word length of editorial corpus: " + str(word_length_average(editorial_tagged_sents))
print "Average word length of review corpus: " + str(word_length_average(review_tagged_sents))

sentence = [("Who","WPO"), ("did","DO"), ("you","PPSS"), ("love","VB"), ("?",".")]
print "Average length of words in single sentence: " + str(single_sent_word_length(sentence))
