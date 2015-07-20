"""
Created on Thu Jul 16 21:58:45 2015

Script that handles operations involving the body of the e-mail, such as
tokenizing, counting words, etc.

@author: Aashish Satyajith
"""

# for tokenize
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

# for reading all the files
from os import listdir
from os.path import isfile, join

# high performance data type to count the number of occurrences of a term
from collections import Counter

# add path to NLTK file
nltk.data.path = ['nltk_data']
# load stopwords
stopwords = set(stopwords.words('english'))

# path for all the training data sets
spam_path = 'data/spam/'
easy_ham_path = 'data/easy_ham/'

# constants for accessing tuple indices in training set
FREQUENCY = 0
FILE_COUNT = 1
    

"""

Hints:

# received help from http://slendermeans.org/ml4h-ch3.html for NLTK

# Note, remove '=' symbols before tokenizing, since these
# sometimes occur within words to indicate, e.g., line-wrapping.
msg_words = set(wordpunct_tokenize(msg.replace('=\\n', '').lower()))

# Get rid of stopwords
msg_words = msg_words.difference(stopwords) 
    
from os import listdir
from os.path import isfile, join
mypath = './data'
files_in_dir = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for files in filepath:
    with open(files, 'r') as f:
        for line in f:
            if 'Abstract' in line:                
                for line in f: # now you are at the lines you want
                    # do work
"""

def get_word_count(message):
    
    """
    Extracts all the words from the given mail and returns a dict of <term>: 
    <number of occurrences> from it.
    """
    
    # thanks http://slendermeans.org/ml4h-ch3.html
    
    # remove '=' symbols before tokenizing, since these
    # sometimes occur within words to indicate, e.g., line-wrapping
    # also remove newlines    
    all_words = wordpunct_tokenize(message.replace('=\\n', '').lower())
    
    # remove the stopwords
    msg_words = [word for word in all_words if word not in stopwords and len(word) > 2]
    
    # count the number of occurrences of each word
    word_count_dict = dict(Counter(msg_words))
    
    return word_count_dict   
    
def make_training_set(path):
    
    """
    Returns a dictionary of <term>: (<total_frequency>, <occurrence>) of all 
    the terms in files contained in the directory specified by path.
    path is mainly directories to the training data for spam and ham folders.
    occurrence is the percentage of documents that have the 'term' in it.
    frequency is the total number of times the 'term' appears across all the
    documents in the path
    """
    
    # initializations
    training_set = {}
    total_frequency = 0

    mails_in_dir = [mail_file for mail_file in listdir(path) if isfile(join(path, mail_file))]
    
    # count of cmds in the directory
    cmds_count = 0
    # total number of files in the directory
    total_file_count = len(mails_in_dir)
    
    
    for mail_name in mails_in_dir:
        if mail_name == 'cmds':
            cmds_count += 1
            continue
        with open(path + mail_name, 'r') as mail_file:
            message = ''
            for line in mail_file:
                if line == '\n':
                    # make a string out of the remaining lines
                    for line in mail_file:
                        message += line
                    # we have the message now
                    # get the word count
                    term_count_dict = get_word_count(message)
                    
                    # add entries to the training set
                    for term in term_count_dict.keys():
                        if term in training_set:
                            training_set[term] = (training_set[term][FREQUENCY] + term_count_dict[term], training_set[term][FILE_COUNT] + 1)
                        else:
                            training_set[term] = (term_count_dict[term], 1)
                        total_frequency += term_count_dict[term]
    
    # reducing the count of cmds files from file count
    total_file_count -= cmds_count
    # calculating the occurrence for each term
    for term in training_set.keys():
        training_set[term] = (training_set[term][FREQUENCY], float(training_set[term][FILE_COUNT]) / total_file_count)
                            
    return training_set
    
print 'Loading training sets...',
spam_training_set = make_training_set(spam_path)
ham_training_set = make_training_set(easy_ham_path)
print 'done.'