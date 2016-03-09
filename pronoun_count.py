"""
Created on 20 Feb 2016
Updated on 09 March 2016
@author: Pat
"""

from tag_set import penn_pron_tags, brown_pron_tags, penn_punct, brown_punct


# calculate average of pronouns per sentence in a corpus
def count_pronouns_per_sentence(tagged_corpus):
    num_of_pronouns = 0
    num_of_sents = 0
    for sent in tagged_corpus:
        num_of_sents += 1.0
        for (word, tag) in sent:
            if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
                num_of_pronouns += 1.0
    if not num_of_pronouns == 0:
        pron_per_sent = num_of_pronouns/num_of_sents
    else:
        pron_per_sent = 0
    return pron_per_sent


# calculate ratio of pronouns per total number of words in a corpus
def count_pronouns_per_words(tagged_corpus):
    num_of_pronouns = 0
    num_of_words = 0
    for sent in tagged_corpus:
        for (word, tag) in sent:
            if not (penn_punct.__contains__(tag) or brown_punct.__contains__(tag)):
                num_of_words += 1.0
            if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
                num_of_pronouns += 1.0
    if not num_of_pronouns == 0:
        pron_per_word_total = num_of_words/num_of_pronouns
    else:
        pron_per_word_total = 0.0
    return pron_per_word_total


# pronouns in a single sentence
def count_pronouns_sent(tagged_sent):
    num_of_pronouns = 0
    for (word, tag) in tagged_sent:
        if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
            num_of_pronouns += 1
    return num_of_pronouns
