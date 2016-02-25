"""
Created on 17 Feb 2016
@author: ankita
"""

import nltk
from collections import Counter
import os
import sys

def read_file():
    newpath = 'C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\OutputFiles'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    list_of_files = os.listdir("InputFiles")
    for x in list_of_files:
        ip = 'C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\InputFiles' + x
        f = open(ip, "r")
        y = os.path.basename(f.name)
        filename = open("C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\OutputFiles" + y + ".txt",'w')
        sys.stdout = filename
        line = f.readline()
        while line:
            text = nltk.word_tokenize(line)
            print text
            tags = nltk.pos_tag(text)
            print tags
            counts = Counter(tag for word,tag in tags)
            print counts
            print '\n'
            line = f.readline()
        f.close()

read_file()

