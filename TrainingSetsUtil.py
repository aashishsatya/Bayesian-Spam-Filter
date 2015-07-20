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

# add path to NLTK file
nltk.data.path = ['nltk_data']
# load stopwords
stopwords = set(stopwords.words('english'))

# path for all the training data sets
spam_path = 'data/spam/'
easy_ham_path = 'data/easy_ham/'

def get_words(message):
    
    """
    Extracts all the words from the given mail and returns it as a set.
    """
    
    # thanks http://slendermeans.org/ml4h-ch3.html
    
    # remove '=' symbols before tokenizing, since these
    # sometimes occur within words to indicate, e.g., line-wrapping
    # also remove newlines    
    all_words = set(wordpunct_tokenize(message.replace('=\\n', '').lower()))
    
    # remove the stopwords
    msg_words = [word for word in all_words if word not in stopwords and len(word) > 2]
    
    return msg_words
    
def get_mail_from_file(file_name):
    
    """
    Returns the entire mail as a string from the given file.
    """
    
    message = ''
    
    with open(file_name, 'r') as mail_file:
        
        for line in mail_file:
            # the contents of the actual mail start after the first newline
            # so find it, and then extract the words
            if line == '\n':
                # make a string out of the remaining lines
                for line in mail_file:
                    message += line
                    
    return message
    
    
    
def make_training_set(path):
    
    """
    Returns a dictionary of <term>: <occurrence> of all 
    the terms in files contained in the directory specified by path.
    path is mainly directories to the training data for spam and ham folders.
    occurrence is the percentage of documents that have the 'term' in it.
    frequency is the total number of times the 'term' appears across all the
    documents in the path
    """
    
    # initializations
    training_set = {}

    mails_in_dir = [mail_file for mail_file in listdir(path) if isfile(join(path, mail_file))]
    
    # count of cmds in the directory
    cmds_count = 0
    # total number of files in the directory
    total_file_count = len(mails_in_dir)
    
    for mail_name in mails_in_dir:
        
        if mail_name == 'cmds':
            cmds_count += 1
            continue
        
        # get the message in the mail
        message = get_mail_from_file(path + mail_name)
        
        # we have the message now
        # get the words in the message
        terms = get_words(message)
                    
        # what we're doing is tabulating the number of files
        # that have the word in them
        # add these entries to the training set
        for term in terms:
            if term in training_set:
                training_set[term] = training_set[term] + 1
            else:
                training_set[term] = 1
    
    # reducing the count of cmds files from file count
    total_file_count -= cmds_count
    # calculating the occurrence for each term
    for term in training_set.keys():
        training_set[term] = float(training_set[term]) / total_file_count
                            
    return training_set

print ''    
print 'Loading training sets...',
spam_training_set = make_training_set(spam_path)
ham_training_set = make_training_set(easy_ham_path)
print 'done.'
print ''