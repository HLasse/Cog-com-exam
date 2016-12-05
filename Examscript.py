#!/usr/bin/python

#import modules
import io, unicodedata
from afinn import Afinn
import os
import re

#add all text files from folder to a list of allFiles
allFiles = []
for root, dirs, files in os.walk('/Users/kennethenevoldsen/Desktop/CogComExam/txt_files'):
    for file in files:
        if file.endswith('.txt'):
            allFiles.append(file)

# apply Afinn da 32
afinn = Afinn(language='da')
# length normalized score
def normScore(text):
    score=afinn.score(text)/len(text.split())
    return score

#cleaner for text
def clean(txt):
    txt = re.sub("[:\.\?()\&%,><@+\/\\\*]", "", txt)
    txt = re.sub("\[.*[\],\S*]", "", txt)
    txt = re.sub("-", "", txt)
    txt = re.sub("'", "", txt)
    txt=txt.lower()
    return txt

for file in allFiles:
    fileDirectory = '/Users/kennethenevoldsen/Desktop/CogComExam/txt_files/'+file
    f = io.open(fileDirectory,'r',encoding='utf8')
    text = f.read()
    text=clean(text)    
    for word in text.split():
        print afinn.score(word), word

#    text = unicodedata.normalize('NFKD', file) # normalize and ascii encode
#    score=normScore(text)
#    print score, file
