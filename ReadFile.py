"""
Created on 17 Feb 2016
@author: ankita
"""

import nltk
from collections import Counter
import os
import sys

def read_file():

    #newpath is the path where the folder for the output files is created
    newpath = 'C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\InputFiles\ParsedFiles'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    os.chdir(r"C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\InputFiles")

    for file in os.listdir("C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\InputFiles"):
        if file.endswith(".txt"):
            f = open(file, "r")
            y = "parsed_" + os.path.basename(f.name)

            filename = open(os.path.join(newpath,y) ,'w')
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
