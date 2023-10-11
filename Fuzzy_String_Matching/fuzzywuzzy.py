#Installing libraries
pip install fuzzywuzzy

#Levenshtein Distance¶
import Levenshtein as lev
​
str1 = "Back"
str2 = "Book"
lev.distance(str1.lower(), str2.lower())

#FuzzyWuzzy
from fuzzywuzzy import fuzz
​
str1 = "Back"
str2 = "Book"
ratio = fuzz.ratio(str1.lower(), str2.lower())
print(ratio)

str1 = "My name is Ana"
str2 = "Ana is my name"
ratio = fuzz.ratio(str1.lower(), str2.lower())
print(ratio)

#Partial Ratio using FuzzyWuzzy
str1 = "My name is Ana"
str2 = "My name is Ana Cox"
p_ratio = fuzz.partial_ratio(str1.lower(), str2.lower())
print(p_ratio)

#Token Sort Ratio using FuzzyWuzzy
str1 = "My name is Ana"
str2 = "Ana is my name"
t_s_ratio = fuzz.token_sort_ratio(str1.lower(), str2.lower())
print(t_s_ratio)

#Token Set Ratio using FuzzyWuzzy
str1 = "My name is Ana"
str2 = "Ana is  my name name"
t_sort_ratio = fuzz.token_sort_ratio(str1, str2)
t_set_ratio = fuzz.token_set_ratio(str1, str2)
print(t_sort_ratio)
print(t_set_ratio)

#Process Module using FuzzyWuzzy
from fuzzywuzzy import process
​
query = "My name is Ana"
choices = ["My name Ana", "My name is Ana", "My Ana"]
process.extract(query, choices)

process.extractOne(query, choices)
