#Importing Libraries
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sbn
import re
import nltk
​
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn import metrics
​
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

nltk.download('stopwords')

#Loading the Data
data = pd.read_csv('/kaggle/input/sentiment-analysis-data/Train.csv')
data.head()

#Data Visualization
fig = plt.figure(figsize = (5, 5))
colors = ["Skyblue", "Pink"]
pos = data[data['label'] == 1]
neg = data[data['label'] == 0]
​
cnt = [pos['label'].count(), neg['label'].count()]
​
legpie = plt.pie(
    cnt, 
    labels = ['Positive', 'Negative'],
    autopct = '%1.1f%%',
    shadow = True,
    colors = colors,
    startangle = 45,
    explode = (0, 0.1)
)

#Text Preprocessing
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emojis = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emojis).replace('-', '')
    return text
​
data['text'] = data['text'].apply(preprocessor)

#To simplify the data and remove unnecessary complexities in our text data
porter = PorterStemmer()
​
def tokenizer(text):
    return text.split()
​
def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]

#Visualize the Negative and Positive Words
stop = stopwords.words('english')
positive_data = data[data['label'] == 1]
positive_data = positive_data['text']
negative_data = data[data['label'] == 0]
negative_data = negative_data['text']
​
def wordCloudDraw(data, color = 'white'):
    words = ' '.join(data)
    cleaned_word = ' '.join([word for word in words.split() if word != 'movie' and word != 'film'])
    word_cloud = WordCloud(
        stopwords = stop,
        background_color = color,
        width = 2500,
        height = 2000
    ).generate(cleaned_word)
    plt.figure(1, figsize = (10, 7))
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()
​
print("Positive words are as follows")
wordCloudDraw(positive_data, 'white')
print("Negative words are as follows")
wordCloudDraw(negative_data)

#Preparing Feature Matrix
tfidf = TfidfVectorizer(
    strip_accents = None,
    lowercase = False, 
    preprocessor = None,
    tokenizer = tokenizer_porter,
    use_idf = True,
    norm = 'l2',
    smooth_idf = True
)
​
y = data.label.values 
x = tfidf.fit_transform(data.text)

#Model Building
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    random_state = 1,
    test_size = 0.5,
    shuffle = False
)

model = LogisticRegressionCV(cv = 6, scoring = 'accuracy', random_state = 0, n_jobs = -1, verbose = 3, max_iter = 500).fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))
