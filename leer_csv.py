# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:04:04 2019

@author: patricio.a.drasal
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:48:47 2019

@author: patricio.a.drasal
"""

### READ TEXT FILES

f=open("alice_in_wonderland.txt", "r")
if f.mode == 'r':
        file_contents =f.read()
        print(file_contents)


### READ CSV FILES


import csv
f=open("prueba.csv", "r")
if f.mode == 'r':
        reader =csv.reader(f,delimiter=',')
        print(reader)



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

## para user con nltk functions como concordancia
textlist = Text(step1)
type(textlist)

## concordancia: concordance shows us every occurrence of a given word, together with some context.
textlist.concordance("alice")
textlist.similar("clear")

textlist.dispersion_plot(["Alice", "rabbit", "cat"])

