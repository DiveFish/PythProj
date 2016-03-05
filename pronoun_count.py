"""
Created on 20 Feb 2016
Updated on 05 March 2016
@author: pat
"""

from corpustags import news_tagged_sents, editorial_tagged_sents, review_tagged_sents
from nps_tags import nps_chat_tagged
from tag_set import penn_pron_tags, brown_pron_tags


def count_pronouns_corpus(tagged_corpus):
    num_of_pronouns = 0
    num_of_sents = 0
    for sent in tagged_corpus:
        num_of_sents += 1.0
        for (word, tag) in sent:
            if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
                num_of_pronouns += 1.0
                # print word + ' ' + tag
            '''
            #to check that no word which should be counted has been missed
            if word == "you":
                print '   ' + word
            '''
    # print num_of_pronouns
    # print num_of_sents
    pron_per_sent = num_of_pronouns/num_of_sents
    return pron_per_sent


def count_pronouns_sent(tagged_sent):
    num_of_pronouns = 0
    for (word, tag) in tagged_sent:
        if (brown_pron_tags.__contains__(tag)) or (penn_pron_tags.__contains__(tag)):
            num_of_pronouns += 1
            # print word + ' ' + tag
        '''
        #to check that no word which should be counted has been missed
        if word == "you":
            print '   ' + word
        '''
    return num_of_pronouns


print 'PRONOUN COUNTS FOR ACCESSED CORPORA'
print 'average of chat pronouns: ' + str(count_pronouns_corpus(nps_chat_tagged))
print 'average of news pronouns: ' + str(count_pronouns_corpus(news_tagged_sents))
print 'average of editorial pronouns: ' + str(count_pronouns_corpus(editorial_tagged_sents))
print 'average of review pronouns: ' + str(count_pronouns_corpus(review_tagged_sents))

sentence = [('Who','WPO'), ('do','DO'), ('you','PPSS'), ('love','VB'), ('?','.')]
print 'Pronouns in a random sentence: ' + str(count_pronouns_sent(sentence))
