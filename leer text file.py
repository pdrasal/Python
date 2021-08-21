# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:48:47 2019

@author: patricio.a.drasal
"""
import nltk
from nltk.book import *
from nltk.corpus import wordnet

### READ TEXT FILES

f=open("carroll-alice.txt", "r")
if f.mode == 'r':
        file_contents =f.read()
        print(file_contents)

##### FIRST SECTION TOKENIZE AND STOP WORDS ##### 

def stop_words(text,lenguage):
    stopwords = set(nltk.corpus.stopwords.words(lenguage))
    stopwords.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    text_new=text.split()    
    content = [w for w in text_new if w.lower() not in stopwords]
    return(content)

#### SECTION LEXICAL DIVERSITY
def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total


print(lexical_diversity(file_contents))
step1=stop_words(file_contents,'english')
freq = nltk.FreqDist(step1)
freq.plot(20, cumulative=False)
print(freq.most_common(50)) 

## para user con nltk functions
textlist = nltk.text(step1)
type(textlist)

## concordancia: concordance shows us every occurrence of a given word, together with some context.
textlist.concordance("alice")
textlist.similar("clear")

textlist.dispersion_plot(["Alice", "rabbit", "cat"])

## wordnets

from nltk.corpus import wordnet as wn
wn.synsets('motorcar')
wn.synsets('automobile')

wn.synset('car.n.01').lemma_names
wn.synsets('car.n.01')

wn.lemma('car.n.01.automobile').name