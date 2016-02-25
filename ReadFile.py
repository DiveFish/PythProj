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
    newpath = 'C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\OutputFiles'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    #"InputFiles" is the folder containing all input files
    list_of_files = os.listdir("InputFiles")
    for x in list_of_files:
        f = open(x, "r") #I get an error here. It cannot recognise the filename. Have tried giving the complete path but same error
        y = os.path.basename(f.name)
        
        #Modify path accordingly to path of output file folder
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

