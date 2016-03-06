"""
Created on 20 Feb 2016
Updated on 06 March 2016
@author: Pat
"""

from tag_set import penn_pron_tags, brown_pron_tags


# calculate average of pronouns per sentence in a corpus
def count_pronouns_corpus(tagged_corpus):
    num_of_pronouns = 0
    num_of_sents = 0
    for sent in tagged_corpus:
        num_of_sents += 1.0
        for (word, tag) in sent:
            if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
                num_of_pronouns += 1.0
    pron_per_sent = num_of_pronouns/num_of_sents
    return pron_per_sent


# calculate ratio of pronouns per total number of words in a corpus
def count_pronouns_per_words(tagged_corpus):
    num_of_pronouns = 0
    num_of_words = 0
    for sent in tagged_corpus:
        for (word, tag) in sent:
            num_of_words += 1.0
            if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
                num_of_pronouns += 1.0
    pron_per_word_total = num_of_words/num_of_pronouns
    return pron_per_word_total


def count_pronouns_sent(tagged_sent):
    num_of_pronouns = 0
    for (word, tag) in tagged_sent:
        if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
            num_of_pronouns += 1
    return num_of_pronouns
