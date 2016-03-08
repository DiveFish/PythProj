"""
Created on 20 Feb 2016
Updated on 24 Feb 2016
@author: kibs
"""

import re


def is_word(string):
    find_letter = re.search('[a-z0-9]', string)
    letter_in_string = bool(find_letter)
    return letter_in_string


# takes a list of words
def ttr_words(text):
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
    return type / tokens


# takes a list of (word, tag)
def ttr_tagged_words(tagged_text):
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
    return type / tokens


# takes a list of lists (sentences) of (word, tag)
def ttr_tagged_sents(tagged_sents):
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
    return type / tokens


# takes list of lists(lists) of words
def ttr_sents(sents):
    tokens = 0.0
    type = 0.0
    word_list = list()
    for sent in sents:
        for word in sent:
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
    return type / tokens
