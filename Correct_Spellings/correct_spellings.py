#Importing the Library
from textblob import TextBlob

#Main Code
words = ['Machne', 'Leearning']
correct_words = []
​
for i in words:
    correct_words.append(TextBlob(i))
​
print("Wrong Words - ", words)
print("Correct Words - ")
for i in correct_words:
    print(i.correct(), end = " ")
