"""
Created on Mon Jul 20 12:14:16 2015

A file that demonstrates the program classifying hard ham mails. The ideal
classification would result in the program classifying all mails as spam, but
this does not happen in practice.

@author: aashishsatya
"""

from SpamClassifier import *

SPAM = 'spam'
HAM = 'ham'

# change it to the type of mails you want to classify
# path to the hard ham mails
spam2_path = 'data/spam_2/'
easy_ham2_path = 'data/easy_ham_2/'
hard_ham2_path = 'data/hard_ham_2/'
hard_ham_path = 'data/hard_ham/'

test_paths = [spam2_path, easy_ham2_path, hard_ham_path, hard_ham2_path]

for mail_path in test_paths:

    mails_in_dir = [mail_file for mail_file in listdir(mail_path) if isfile(join(mail_path, mail_file))]
    
    results = {}
    results[SPAM] = 0
    results[HAM] = 0
    
    print('Running classifier on files in', mail_path[5:-1], '...')

    for mail_name in mails_in_dir:
        
        if mail_name == 'cmds':
            continue
        
        mail_msg = get_mail_from_file(mail_path + mail_name)
        
        # 0.2 and 0.8 because the ratio of samples for spam and ham were the same
        spam_probability = classify(mail_msg, spam_training_set, 0.2)
        ham_probability = classify(mail_msg, ham_training_set, 0.8)
        
        if spam_probability > ham_probability:
            results[SPAM] += 1
        else:
            results[HAM] += 1
            
        total_files = results[SPAM] + results[HAM]
        spam_fraction = float(results[SPAM]) / total_files
        ham_fraction = 1 - spam_fraction
                
    print('Fraction of spam messages =', spam_fraction)
    print('Fraction of ham messages =', ham_fraction)
    print('')