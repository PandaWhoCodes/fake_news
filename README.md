# Overview:

Identifying public misinformation is a complicated and challenging task, and with the growth of the internet the spread of misinformation happens too quickly on a large scale.

To rectify this problem several people have come up with their solutions -  Most of them being crowdsourced like <https://www.altnews.in/> or BS Detector. They are web platforms dedicated to verifying and debunking the scourge of fake news in circulation.

The entire process involves the following:

1.  News article received
2.  A volunteer takes the article
3.  Does fact check for the entire article
4.  Determines if the article is Fake or not.

# The problem:

1.  Too many fake articles
2.  Each article takes too much time for fact checking
3.  Number of volunteers is very small
4.  Classifying fake news can be tough - https://miguelmalvarez.com/2017/03/23/how-can-machine-learning-and-ai-help-solving-the-fake-news-problem/

Read the above article to understand different types of fake news

# Our Solution:

Our machine learning model is made to help the fact checkers and not replace them. It reduces the time to to check articles by giving insights to the fact checker as to what level of scrutiny it should use for the particular article.

# Technical details:
NOTE: perceptron has been replaced with - SGDClassifier (to reduce Out of memory error)
The entire project can be categorized under two words - [Stance Detection](https://web.stanford.edu/class/cs224n/reports/2754942.pdf)
Stance detection  can be defined as detecting whether the author of a piece of text is in favor of the given target or against it.
Our stance detection model is an end to end model with lexical and feature extractors that feed the multi layer perceptron.
In machine learning, the perceptron is an algorithm for supervised learning of binary classifiers. It is a type of linear classifier.
To understand a little better on how a perceptron works(kinda) read a little about [Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)- a probabilistic formula that learns and produces an output based on the inputs given.

# Working:

## Dataset used :
https://www.kaggle.com/mrisdal/fake-news/data

1.  Feature Extraction

The first step is the feature extraction step is done with the help of [two bag of words](https://www.youtube.com/watch?v=T1O3ikmTEdA) (see the peter norvig video to understand it a bit)

From the bag of words we will extract two things

1.  Word Frequencies
2.  Inverse word frequencies - [Sklearn documentation](http://scikit-learn.org/stable/modules/feature_extraction.html)

Since we cannot feed the words directly to the machine, we need to vectorize it. To vectorize it we use [TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

We tokenize the headline and body texts as well as derive the relevant vectors. For the TF(term frequencies)vectors, we extract a vocabulary of around 5,000 most frequent words in the training set and exclude stop words(from nltk.corpus).
The same is done for the Inverse word freq vectors.
The TF vectors and the TF-IDF cosine similarity are concatenated in a feature vector and then fed into the classifier.
2\. Train
The features are then fed to the machine with labels of biased and not fake.
3\. Predict

ALGO:

From the frontend app take the following as input

1.  URL

And then extract the following from the url

1.  Page title
2.  Page text

Feed the page title and page text to our ML Model ->
Get the prediction score based on which display the proper score on the website(console).
DEMO VIDEO

https://youtu.be/_xxYfW6k7TU