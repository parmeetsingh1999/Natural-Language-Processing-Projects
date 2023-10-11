#Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
​
from wordcloud import WordCloud

#Loading the dataset
data = pd.read_csv('/kaggle/input/top-play-store-games/android-games.csv')
data.head()

#Data Preprocessing
data.isna().sum()

text = " ".join(cat.split()[1] for cat in data.category)
print(text)

#Creating word cloud
word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)

plt.imshow(word_cloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()
