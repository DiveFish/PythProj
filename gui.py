"""
Created in Feb 2016
Updated on 09 March 2016
@author:pat
"""

import random
from Tkinter import *

from corpora_by_level_and_register import news_easy, news_advanced, news_difficult, editorial_easy, editorial_advanced, \
    editorial_difficult, reviews_easy, reviews_advanced, reviews_difficult, government_easy, government_advanced, \
    government_difficult, chat_easy, chat_advanced, chat_difficult
from pronoun_count import count_pronouns_per_sentence
from read_file import read_file
from sent_feats import sent_length_average, word_length_average
from tag_set import penn_punct, brown_punct
from type_token_ratio import ttr_tagged_sents

master = Tk()


def print_sentences():
    chosen_level = str(level.get())
    chosen_register = str(register.get())
    if chosen_level == "easy" or chosen_level == "advanced":
        print "\033[1m \n 5 random sentences from an "+chosen_level+" "+chosen_register+" text: \033[0m"
    elif chosen_level == "difficult":
        print "\033[1m \n 5 random sentences from a "+chosen_level+" "+chosen_register+" text: \033[0m"
    else:
        print "Error. \n"
    if chosen_register == "news":
        if chosen_level == "easy":
            for sentence in random.sample(news_easy, 5):
                print_sentence(sentence)
        elif chosen_level == "advanced":
            for sentence in random.sample(news_advanced, 5):
                print_sentence(sentence)
        elif chosen_level == "difficult":
            for sentence in random.sample(news_difficult, 5):
                print_sentence(sentence)
        else:
            print "Error. \n"
    elif chosen_register == "editorial":
        if chosen_level == "easy":
            for sentence in random.sample(editorial_easy, 5):
                print_sentence(sentence)
        elif chosen_level == "advanced":
            for sentence in random.sample(editorial_advanced, 5):
                print_sentence(sentence)
        elif chosen_level == "difficult":
            for sentence in random.sample(editorial_difficult, 5):
                print_sentence(sentence)
        else:
            print "Error. \n"
    elif chosen_register == "reviews":
        if chosen_level == "easy":
            for sentence in random.sample(reviews_easy, 5):
                print_sentence(sentence)
        elif chosen_level == "advanced":
            for sentence in random.sample(reviews_advanced, 5):
                print_sentence(sentence)
        elif chosen_level == "difficult":
            for sentence in random.sample(reviews_difficult, 5):
                print_sentence(sentence)
        else:
            print "Error. \n"
    elif chosen_register == "government":
        if chosen_level == "easy":
            for sentence in random.sample(government_easy, 5):
                print_sentence(sentence)
        elif chosen_level == "advanced":
            for sentence in random.sample(government_advanced, 5):
                print_sentence(sentence)
        elif chosen_level == "difficult":
            for sentence in random.sample(government_difficult, 5):
                print_sentence(sentence)
        else:
            print "Error. \n"
    elif chosen_register == "webchat":
        if chosen_level == "easy":
            for sentence in random.sample(chat_easy, 5):
                print_sentence(sentence)
        elif chosen_level == "advanced":
            for sentence in random.sample(chat_advanced, 5):
                print_sentence(sentence)
        elif chosen_level == "difficult":
            for sentence in random.sample(chat_difficult, 5):
                print_sentence(sentence)
        else:
            print "Error. \n"
    else:
        print "Error. \n"


# helper-method for printing one sentence in print_sentences
def print_sentence(sentence):
    single_sentence = ""
    for (word, tag) in sentence:
        if not (penn_punct.__contains__(tag) or brown_punct.__contains__(tag)):
            single_sentence += str(word)+" "
        else:
            single_sentence = single_sentence[:len(single_sentence)-1]+str(word)+" "
    print single_sentence


def save_sentences_to_file():
    chosen_level = str(level.get())
    chosen_register = str(register.get())
    sentence_list = list()
    wr = open(fileName_sentences.get(), "w")
    if chosen_register == "news":
        if chosen_level == "easy":
            for sentence in random.sample(news_easy, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "advanced":
            for sentence in random.sample(news_advanced, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "difficult":
            for sentence in random.sample(news_difficult, 5):
                sentence_list.append(save_sentence(sentence))
        else:
            wr.write("Error. \n")
    elif chosen_register == "editorial":
        if chosen_level == "easy":
            for sentence in random.sample(editorial_easy, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "advanced":
            for sentence in random.sample(editorial_advanced, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "difficult":
            for sentence in random.sample(editorial_difficult, 5):
                sentence_list.append(save_sentence(sentence))
        else:
            wr.write("Error. \n")
    elif chosen_register == "reviews":
        if chosen_level == "easy":
            for sentence in random.sample(reviews_easy, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "advanced":
            for sentence in random.sample(reviews_advanced, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "difficult":
            for sentence in random.sample(reviews_difficult, 5):
                sentence_list.append(save_sentence(sentence))
        else:
            wr.write("Error. \n")
    elif chosen_register == "government":
        if chosen_level == "easy":
            for sentence in random.sample(government_easy, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "advanced":
            for sentence in random.sample(government_advanced, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "difficult":
            for sentence in random.sample(government_difficult, 5):
                sentence_list.append(save_sentence(sentence))
        else:
            wr.write("Error. \n")
    elif chosen_register == "webchat":
        if chosen_level == "easy":
            for sentence in random.sample(chat_easy, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "advanced":
            for sentence in random.sample(chat_advanced, 5):
                sentence_list.append(save_sentence(sentence))
        elif chosen_level == "difficult":
            for sentence in random.sample(chat_difficult, 5):
                sentence_list.append(save_sentence(sentence))
        else:
            wr.write("Error. \n")
    else:
        wr.write("Error. \n")
    if chosen_level == "easy" or chosen_level == "advanced":
        wr.write("5 RANDOM SENTENCES FROM AN "+chosen_level+" "+chosen_register+" TEXT: \n")
    elif chosen_level == "difficult":
        wr.write("5 RANDOM SENTENCES FROM A "+chosen_level+" "+chosen_register+" TEXT: \n")
    else:
        print "Error. \n"
    for item in sentence_list:
        wr.write("  "+str(item)+"\n")
    wr.close()


# helper-method for saving one sentence in save_sentences_to_file
def save_sentence(sentence):
    single_sentence = ""
    for (word,tag) in sentence:
        if not (penn_punct.__contains__(tag) or brown_punct.__contains__(tag)):
            single_sentence += str(word)+" "
        else:
            single_sentence = single_sentence[:len(single_sentence)-1]+str(word)+" "
    return single_sentence


def print_analysis():
    tagged_file = read_file(directory.get())
    if tagged_file.__len__() == 0:
        print "ERROR: Empty file."
    else:
        sent_length = sent_length_average(tagged_file)
        word_length = word_length_average(tagged_file)
        pron_count = count_pronouns_per_sentence(tagged_file)
        ttr = ttr_tagged_sents(tagged_file)
        print "The average sentence length is "+str(sent_length)
        print "The average word length is "+str(word_length)
        print "The number of pronouns per number of sentences is "+str(pron_count)
        print "The type-token ratio is "+str(ttr)
        trad_complexity = (sent_length+word_length)/2
        lex_complexity = (pron_count+(1/ttr))/2
        complexity = (sent_length+word_length+pron_count+(1/ttr))/4
        if complexity < 5:
            print "\033[1m ->> The overall complexity of the given text is easy \033[0m \n"
        elif 5 <= complexity < 8:
            print "\033[1m ->> The overall complexity of the given text is advanced \033[0m \n"
        else:
            print "\033[1m ->> The overall complexity of the given text is difficult \033[0m \n"
        print "<-- The TRADITIONAL complexity is "+str(trad_complexity)+"\n"
        print "<-- The LEXICAL complexity is "+str(lex_complexity)+"\n"


def save_analysis_to_file():
    wr = open(fileName_analysis.get(), "w")
    tagged_file = read_file(directory.get())
    if tagged_file.__len__() == 0:
        wr.write("ERROR: Empty file.")
    else:
        sent_length = sent_length_average(tagged_file)
        word_length = word_length_average(tagged_file)
        pron_count = count_pronouns_per_sentence(tagged_file)
        ttr = ttr_tagged_sents(tagged_file)
        wr.write("The average sentence length is "+str(sent_length)+"\n")
        wr.write("The average word length is "+str(word_length)+"\n")
        wr.write("The number of pronouns per number of sentences is "+str(pron_count)+"\n")
        wr.write("The type-token ratio is "+str(ttr)+"\n")
        trad_complexity = (sent_length+word_length)/2
        lex_complexity = (pron_count+(1/ttr))/2
        complexity = (sent_length+word_length+pron_count+(1/ttr))/4
        if complexity < 5:
            wr.write("->> The OVERALL COMPLEXITY of the given text is EASY \n")
        elif 5 <= complexity < 8:
            wr.write("->> The OVERALL COMPLEXITY of the given text is ADVANCED \n")
        else:
            wr.write("->> The OVERALL COMPLEXITY of the given text is DIFFICULT \n")
        wr.write("<-- The TRADITIONAL complexity is "+str(trad_complexity)+"\n")
        wr.write("<-- The LEXICAL complexity is "+str(lex_complexity)+"\n")
    wr.close()


Label(text="\n").pack()
Label(master, text="Get a selection of five sentences \n with a learner level and register of your choice!",
      font = "normal 11 bold").pack()


# drop down for choosing level
Label(text="Level: ").pack()
level = StringVar(master)
level.set("easy") # initial value
OptionMenu(master, level, "easy", "advanced", "difficult").pack()


# drop-down menu for choosing register
Label(text="Register: ").pack()
register = StringVar(master)
register.set("webchat") # initial value
OptionMenu(master, register, "webchat", "news", "editorial", "reviews", "government").pack()
Label(text="\n").pack()


# button to print matching sentences to SCREEN
Button(master, text="Print matching sentences to screen!", command=print_sentences).pack()

Label(text="or").pack()

# field to enter file name where output will be saved
Label(master, text="Name an output file here (include .txt): ").pack()
fileName_sentences=Entry(master)
fileName_sentences.pack()
# button to save matching sentences to a FILE
Button(master, text="...and save matching sentences to a file!", command=save_sentences_to_file).pack()


Label(text="\n").pack()


# field to enter directory of files for which user wants complexity level
Label(master, text="Want a text of your own evaluated? \n Just enter the directory of the .txt file(s) here: ",
      font = "normal 11 bold").pack()
directory=Entry(master)
directory.pack()
Label(text="\n").pack()

# button to print matching sentences to SCREEN
Button(master, text="Print results of analysis to screen!", command=print_analysis).pack()

Label(text="or").pack()

# field to enter file name where output will be saved
Label(master, text="Name an output file here (include .txt): ").pack()
fileName_analysis=Entry(master)
fileName_analysis.pack()
# button to save matching sentences to a FILE
Button(master, text="...and save results of analysis to a file!", command=save_analysis_to_file).pack()

f = Frame(master,height=40, width=300)  # use only integers here
f.pack_propagate(0)
f.pack()

master.title("Complexity Analysis")
mainloop()
