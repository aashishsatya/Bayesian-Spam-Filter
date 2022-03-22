# Bayesian Spam Filter

#### NOTE: This was a hobby project, so I do not have any associated project report.

###### Dependencies: NLTK (Natural Language Toolkit) for Python.

An implementation of a Spam Filter in Python that uses the Naive Bayes Model to classify emails as spam or ham.

The program uses a small portion of NLTK to tokenize and clean out the "noise" words that may appear across the text.

#### Reference:

The reference I used was Machine Learning for Hackers by Drew Conway and John Myles White, Chapter 3. The code is in R but should be easy to follow.

The data sets were obtained from the SpamAssassin Public Corpus, which can be found [here](http://spamassassin.apache.org/old/publiccorpus/).

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

#### Acknowledgements

Thanks Vivian Bi Fang Lim for pointing out an error when porting to Python 3. This was fixed on March 23, 2022.

Feel free to contact me at ankarathaashish@gmail.com for suggestions for improvement or bug reports.


