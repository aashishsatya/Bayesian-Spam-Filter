# Bayesian Spam Filter

###### NOTE: NLTK (Natural Language Toolkit) for Python is required.

An implementation of a Spam Filter in Python that uses the Naive Bayes Model to classify emails as spam or ham.

The program uses a small portion of NLTK to tokenize and clean out the "noise" words that may appear across the text.

#### Reference:

The reference I used was Machine Learning for Hackers by Drew Conway and John Myles White, Chapter 3. The code is in R but should be easy to follow. 

The data sets were obtained from the SpamAssassin Public Corpus, which can be found [here](http://spamassassin.apache.org/old/publiccorpus/).

Also this was a hobby project, so I do not have any associated project report.

#### Program Demo:

Simply run the script 'ClassifierDemo.py' once you're in the program directory:

```
python ClassifierDemo.py
```

As the results will show, the classifier has roughly 90% success in distinguishing ham and spam from hard ham mails.

#### Running the program:

You will have to uncomment the last few lines in the script Classifier.py. Then simply run the command

```
python SpamClassifier.py
```

and you should be good to go.

As always, feel free to contact me at ankarathaashish@gmail.com for suggestions for improvement or bug reports. Thank you!!


