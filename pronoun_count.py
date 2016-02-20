'''
Created on 20 Feb 2016
@author: pat
'''
from corpustags import news_tagged_sents, editorial_tagged_sents, review_tagged_sents
from nps_tags import nps_chat_tagged
from tag_set import penn_pron_tags, brown_pron_tags

print 'PRONOUN COUNTS FOR ACCESSED CORPORA'

nps_chat_pron_count = 0
for sent in nps_chat_tagged:
    for (word, tag) in sent:
        if tag[:2] in penn_pron_tags:
            nps_chat_pron_count = nps_chat_pron_count + 1
print 'chat pronouns: '+str(nps_chat_pron_count)

news_pron_count = 0
for sent in news_tagged_sents:
    for (word, tag) in sent:
        if tag[:2] in brown_pron_tags:
            news_pron_count = news_pron_count + 1
            #print word + ' ' + tag
print 'news pronouns: '+str(news_pron_count)

editorial_pron_count = 0
for sent in editorial_tagged_sents:
    for (word, tag) in sent:
        if tag[:2] in brown_pron_tags:
            editorial_pron_count = editorial_pron_count + 1
            #print word + ' ' + tag
print 'editorial pronouns: '+str(editorial_pron_count)

review_pron_count = 0
for sent in review_tagged_sents:
    for (word, tag) in sent:
        if tag[:2] in brown_pron_tags:
            review_pron_count = review_pron_count + 1
            #print word + ' ' + tag

print 'review pronouns: '+str(review_pron_count)


