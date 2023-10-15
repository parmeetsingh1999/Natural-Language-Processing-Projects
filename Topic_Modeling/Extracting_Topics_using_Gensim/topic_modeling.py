#Import Libraries
import numpy as np
import string
import re
import gensim
import nltk
import spacy

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from gensim import corpora
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
D5 = "This blueberry milkshake is so good! Try reading Dr. Joe Dispenza’s books. His work is such a game-changer! His books helped to learn so much about how our thoughts impact our biology and how we can all rewire our brains."

corpus = [D1, D2, D3, D4, D5]
print(corpus)

#Text Processing
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
  stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
  punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
  normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
  return normalized

clean_corpus = [clean(doc).split() for doc in corpus]
print(clean_corpus)

#Creating Document Term Matrix
dict_ = corpora.Dictionary(clean_corpus)
print(dict_)

for i in dict_.values():
  print(i)

#Converting list of documents (corpus) into Document Term Matrix using the dictionary
doc_term_matrix = [dict_.doc2bow(i) for i in clean_corpus]
print(doc_term_matrix)

#Implementation of LDA
lda = gensim.models.ldamodel.LdaModel
model = lda(doc_term_matrix, num_topics = 6, id2word = dict_, passes = 1, random_state = 0, eval_every = None)
model.print_topics()

#Extracting Topics from the Corpus
print(model.print_topics(num_topics = 6, num_words = 5))

#Assigning the Topics to the Documents
count = 0

for i in model[doc_term_matrix]:
  print("Doc: ", count, i)
  count += 1
