"""
Created on 8 March 2016
@author: ankita
"""

import nltk
from collections import Counter
import os
import sys
import ntpath


def read_file(path):
    
    user_file = ntpath.basename(path)
    if user_file.endswith(".txt"):
        f = open(user_file, "r")
        parsed_list = list()
        line = f.readline()
        while line:
            text = nltk.word_tokenize(line)

            tags = nltk.pos_tag(text)
            parsed_list = parsed_list + tags

            line = f.readline()
        f.close()
    return parsed_list

# enter complete path of input file in place of ...
for item in read_file('...'):
    print item

