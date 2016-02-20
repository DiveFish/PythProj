'''
Created on 20 Feb 2016
@author: pat
'''
from corpustags import news_tagged_sents, editorial_tagged_sents, review_tagged_sents
from nps_tags import nps_chat_tagged
from tag_set import penn_pron_tags, brown_pron_tags

def count_pronouns(tagged_corpus):
    num_of_pronouns = 0
    for sent in tagged_corpus:
        for (word, tag) in sent:
            if (tag in brown_pron_tags) or (tag in penn_pron_tags):
                num_of_pronouns = num_of_pronouns + 1
                print word + ' ' + tag
    return num_of_pronouns

print 'PRONOUN COUNTS FOR ACCESSED CORPORA'
print 'chat pronouns: ' + str(count_pronouns(nps_chat_tagged))
print 'news pronouns: ' + str(count_pronouns(news_tagged_sents))
print 'editorial pronouns: ' + str(count_pronouns(editorial_tagged_sents))
print 'review pronouns: ' + str(count_pronouns(review_tagged_sents))
