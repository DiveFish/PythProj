"""
Created on 21 Feb 2016
Updated on 05 March 2016
@author: Pat
"""

# from corpustags import news_tagged_sents, editorial_tagged_sents, review_tagged_sents
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
