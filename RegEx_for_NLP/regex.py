#Importing libraries
import re
import emoji

#URL
def findUrl(string):
    text = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F]))+', string)
    return "".join(text)
​
example = "I love https://www.google.com/"
findUrl(example)

#Emoticons
def findEmoji(text):
    emo_text = emoji.demojize(text)
    line = re.findall(r':(.*?):', emo_text)
    return line
​
example = "I love ⚽ very much 😁"
findEmoji(example)

Email
def findEmail(text):
    line = re.findall(r'\w+@\w+\.\w+', str(text))
    return ",".join(line)
​
example = "My gmail is dayum12345@gmail.com"
findEmail(example)

#Hash
def findHash(text):
    line = re.findall(r'(?<=#)\w+', text)
    return " ".join(line)
​
example = "#Sushant is trending now in the world"
findHash(example)

#Mentions
def findMentions(text):
    line = re.findall(r'(?<=@)\w+', text)
    return " ".join(line)
​
example = "@Ana, please help"
print(findMentions(example))

#Number
def findNumber(text):
    line = re.findall(r'[0-9]+', text)
    return " ".join(line)
​
example = "8865342 sq. km of area washed away in floods"
findNumber(example)

#Phone Number
def findPhoneNumber(text):
    line = re.findall(r'\b\d{10}\b', text)
    return " ".join(line)
​
example = "9876543210 is a phone number of PMO office"
findPhoneNumber(example)

#Non-Alphanumeric
def findNonAN(text):
    line = re.findall("[^A-Za-z0-9 ]", text)
    return line
​
​
example = "Twitter has lots of @ and # in posts.(2021 year is not good)"
findNonAN(example)

#Year
def findYear(text):
    line = re.findall(r'(19[4-9][0-9]|20[0-1][0-9]|2020)', text)
    return " ".join(line)
​
example = "My DOB is 1999"
print(findYear(example))

#Punctuations
def findPunc(text):
    line = re.findall(r'[!"$%&\'()*+,-./:;=#@?[\]^_`{|}~]', text)
    return list(" ".join(line))
​
example = "Corona virus kiled #24506 people. #Corona is un(tolerable)"
print(findPunc(example))

#Repetitive Character
def rep(text):
    grp = text.group(0)
    if len(grp) > 1:
        return grp[0:1]
​
def uniqueChar(rep, sentence):
    convert = re.sub(r'(\w)\1+', rep, sentence)
    return convert
​
example = "heyyy this is a verrrry loong texttt"
uniqueChar(rep, example)

#Number Greater
def numGreater(text):
    line = re.findall(r'9[3-9][0-9]|[1-9]\d{3,}', text)
    return " ".join(line)
​
example = "Height of this bridge is 935m. Width of this bridge is 30 metre. It used 9274kg of steel."
numGreater(example)

#Number Lesser
def numLesser(text):
    only_num = []
    for i in text.split():
        line = re.findall(r'^(9[0-2][0-0]|[1-8][0-9]|[1-9][0-9])$', i)
        only_num.append(line)
        all_num = [",".join(x) for x in only_num if x != []]
    return " ".join(all_num)
​
example = "There are some countries where less than 920 cases exist with 1100 observations"
numLesser(example)

#Dates
def findDates(text):
    line = re.findall(r'(0[1-9]|1[0-2])/(3[01]|[12][0-9]|0[1-9])/([0-9]{4})', text)
    return line
​
example = "Todays date is 06/21/2021 for format mm/dd/yyyy, not 31/09/2020"
findDates(example)

#Only Words
def onlyWords(text):
    line = re.findall(r'\b[^\d\W]+\b', text)
    return " ".join(line)
​
example = "Harish reduced his weight from 100 Kg to 75 kg."
onlyWords(example)

#Only Numbers
def onlyNumbers(text):
    line = re.findall(r'\b\d+\b', text)
    return " ".join(line)
​
example = "Harish reduced his weight from 100 Kg to 75 kg."
onlyNumbers(example)

#Pick Sentences
def pickOnlyKeySentences(text, keyword):
    line = re.findall(r'([^.]*)' + keyword + '[^.]*', text)
    return line
​
example = "People are fighting with covid these days. Economy has fallen down. How will we survive covid"
pickOnlyKeySentences(example, 'covid')

#Caps Lock Words
def findCaps(text):
    line = re.findall(r'\b[A-Z]\w+', text)
    return line
​
example = "Ajit Doval is the best National Security Advisor so far."
findCaps(example)

#Tags
def removeTag(text):
    line = re.sub('<.*?>', '', text)
    return line
​
example = "Markdown sentences use <br> for breaks and <i> </i> for italics"
removeTag(example)

#IP Address
def ipAddress(text):
    line = re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', text)
    return line
​
example = "My public IP address is 165.19.120.1"
ipAddress(example)

#MAC Address
def macAddress(text):
    line = re.findall('(?:[0-9a-fA-F]:?){12}', text)
    return line
​
example = "MAC ADDRESSES of this TOSHIBA laptop is 00:00:5e:00:53:af."
macAddress(example)

#PAN Validation
def validPan(text):
    line = re.findall(r'^([A-Z]){5}([0-9]){4}([A-Z]){1}$', text)
    if line != []:
        print("{} is valid PAN number".format(text))
    else:
        print("{} is not a valid PAN number".format(text))
​
validPan("ABCED3193P")
validPan("lEcGD012eg")

#Percentage
def findPercent(text):
    line = re.findall(r'\b(100|[1-9][0-9]|[0-9])%', text)
    return line
​
example = "COVID recovery rate is now 76%. But death rate is 4%"
findPercent(example)

#File Format
def findFiles(text):
    line = re.findall(r'([a-zA-Z0-9_]+).(jpg|png|gif|jpeg|pdf|ipynb|py)', text)
    all_files = []
    for i in range(len(line)):
        all_files.append('.'.join(line[i]))
    return all_files
​
example = "This image file name is cheatsheet.png . Titanic.py file is most common among beginners."
findFiles(example)
