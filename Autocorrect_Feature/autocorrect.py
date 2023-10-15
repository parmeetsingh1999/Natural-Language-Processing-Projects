#Installing Libraries and Packages
pip install textdistance

#Importing Libraries
import numpy as np
import pandas as pd
import textdistance
import re
import os
​
from collections import Counter
​
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#Loading the Data
words = []
with open('/kaggle/input/book-data/book.txt', 'r') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall('\w+', file_name_data)

#Text Data Preprocessing
vocab = set(words)
print("Top ten words in the text are: ", words[0:10])
print("Total unique words are ", len(vocab))

word_freq ={}
word_freq = Counter(words)
print(word_freq.most_common()[0:10])

#Relative Frequency of Words
probs = {}
total = sum(word_freq.values())
for i in word_freq.keys():
    probs[i] = word_freq[i] / total

#Finding Similar Words
def autocorrect(input_word):
    input_word = input_word.lower()
    if input_word in vocab:
        return ("Your word seems to be correct")
    else:
        sim = [1 - (textdistance.Jaccard(qval = 2).distance(i, input_word)) for i in word_freq.keys()]
        df = pd.DataFrame.from_dict(probs, orient = 'index').reset_index()
        df = df.rename(columns = {'index': 'Word', 0: 'Prob'})
        df['Similarity'] = sim
        output = df.sort_values(['Similarity', 'Prob'], ascending = False).head()
        return (output)

autocorrect('neverteless')
