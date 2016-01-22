'''
Created on 22 Jan 2016

@author: kibs
'''

import nltk
from nltk.corpus import nps_chat

'''
Files in the corpus:
10-19-20s_706posts.xml
10-19-30s_705posts.xml
10-19-40s_686posts.xml
10-19-adults_706posts.xml
10-24-40s_706posts.xml
10-26-teens_706posts.xml
11-06-adults_706posts.xml
11-08-20s_705posts.xml
11-08-40s_706posts.xml
11-08-adults_705posts.xml
11-08-teens_706posts.xml
11-09-20s_706posts.xml
11-09-40s_706posts.xml
11-09-adults_706posts.xml
11-09-teens_706posts.xml
'''


# putting all tagged posts from the nps_chat corpus into one list
nps_chat_tagged = list()

for fileid in nps_chat.fileids():
    print fileid
    for post in nps_chat.tagged_posts(fileid):
        nps_chat_tagged.append(post)
    print str(len(nps_chat_tagged))


print nps_chat_tagged[0]
# tags can be retrieved in the same way as the Brown corpus

    
