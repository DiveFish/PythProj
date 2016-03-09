"""
Created on 9 March 2016
@author: ankita
"""

from collections import Counter
import nltk
import os
import sys
import ntpath

def read_input(path):
    if os.path.isfile(path):
        read_file(path)
    else:
        read_dir(path)

def read_file(path):
    #os.getcwd()
    user_file = ntpath.basename(path)
    if user_file.endswith(".txt"):
        f = open(user_file, "r")
        parsed_list = list()
        line = f.readline()
        while line:
            text = nltk.word_tokenize(line)

            tags = nltk.pos_tag(text)
            parsed_list.append(tags)
            line = f.readline()
        f.close()
    for item in parsed_list:
        print item


def read_dir(path):

    #newpath is the path where the folder for the output files is created
    newpath = path
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


read_input('C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\input.txt')
read_input('C:\Users\Ankita\Desktop\WS 2015_16\Python\Project\Proj\InputFiles\ParsedFiles')
