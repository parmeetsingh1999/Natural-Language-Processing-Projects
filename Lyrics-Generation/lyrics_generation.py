# Importing libraries
import numpy as np
import requests 

# Importing dataset
data = requests.get("https://raw.githubusercontent.com/coding-blocks-archives/ML-Noida-2019-June-Two/master/datasets/speeches/speech.txt")
data = data.text
print(data)
print(data[1000:5000])

# To get the number of occurence of different set of strings in the dataset
def generateTable(data,k=5):
    T = {}
    for i in range(len(data)-k):
        X = data[i: i+k]
        y = data[i+k]
        if T.get(X) is None:
            T[X] = {}
            T[X][y] = 1
        else:
            if T[X].get(y) is None:
                T[X][y] = 1
            else:
                T[X][y] += 1
    return T
temp = "Yo man"
T = generateTable(data.lower())
print(T)

# Prediction
seed = "india is my country"
k = 4
print(seed[-k:])
possibilities = T['ntry']
freq = list(possibilities.values())
print(freq)
probabs = [ele/sum(freq) for ele in freq]
print(probabs)
np.random.choice(list(possibilities.keys()), p = probabs)

def prediction(seed, k=5):
    inp = seed[-k:]
    possibilities = T[inp]
    freq = list(possibilities.values())
    options = list(possibilities.keys())
    probabs = [ele/sum(freq) for ele in freq]
    next_char = np.random.choice(options, p= probabs)
    return next_char

seed = "India is my country"
next_char = prediction(seed)
seed = seed + next_char
next_char = prediction(seed)
seed = seed+next_char
seed = 'dear'
for i in range(1000):
    next_char = prediction(seed)
    seed = seed+next_char
