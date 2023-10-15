#Importing Libraries
import numpy as np
import pandas as pd
import re
import string
import spacy
import nltk

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from warnings import filterwarnings

filterwarnings('ignore')

nltk.download('wordnet')
nltk.download('stopwords')

#Loading the dataset
nlp = spacy.load('en_core_web_sm')

D1 = "I want to watch a movie this weekend."
D2 = "I went shopping yesterday. New Zealand won the World Test Championship by beating India by eight wickets at Southampton."
D3 = "I don’t watch cricket. Netflix and Amazon Prime have very good movies to watch."
D4 = "Movies are a nice way to chill however, this time I would like to paint and read some good books. It’s been long!"
D5 = "This blueberry milkshake is so good! Try reading Dr. Joe Dispenza’s books."

corpus = [D1, D2, D3, D4, D5]
print(corpus)

#Text Processing
#Stop loss words
stop = set(stopwords.words('english'))

#Punctuation
exclude = set(string.punctuation)

#Lemmatization
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

clean_corpus = [clean(doc).split() for doc in corpus]
print(clean_corpus)

#Convert Text to Numerical Representation
#Converting the clean preprocessed corpus to array
#Converting text into numerical representation
tf_idf_vectorizer = TfidfVectorizer(tokenizer = lambda doc: doc, lowercase = False)
#Converting text into numerical representation
cv_vectorizer = CountVectorizer(tokenizer = lambda doc: doc, lowercase = False)

#Array from TF-IDF Vectorizer
tf_idf_arr = tf_idf_vectorizer.fit_transform(clean_corpus)
#Array from Count Vectorizer
cv_arr = cv_vectorizer.fit_transform(clean_corpus)

print(tf_idf_arr)
print(cv_arr)

#Creating vocabulary array which will represent all the corpus
vocab_tf_idf = tf_idf_vectorizer.get_feature_names_out()
print(vocab_tf_idf)

display(len(vocab_tf_idf))
display(len(vocab_cv))

#Implementation of LDA
model = LatentDirichletAllocation(n_components = 6, max_iter = 20, random_state = 20)
x_topics = model.fit_transform(tf_idf_arr)
topic_words = model.components_

#Retrieve the Topics
n_top_words = 5
for i, topic_dist in enumerate(topic_words):
  sorted_topic_dist = np.argsort(topic_dist)
  topic_words = np.array(vocab_tf_idf)[sorted_topic_dist]
  topic_words = topic_words[:-n_top_words:-1]
  print("Topic", str(i + 1), topic_words)

#Annotating the Topics in the Documents
doc_topic = model.transform(tf_idf_arr)

for n in range(doc_topic.shape[0]):
  topic_doc = doc_topic[n].argmax()
  print("Document", n+1, " -- Topic: ", topic_doc)
