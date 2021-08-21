#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request
import nltk
nltk.download('stopwords')
 
##### FIRST SECTION TOKENIZE AND STOP WORDS ##### 

def stop_words(text,lenguage):
    stopwords = set(nltk.corpus.stopwords.words(lenguage))
    stopwords.update(['.','=', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    text_new=text.split()    
    content = [w for w in text_new if w.lower() not in stopwords]
    return(content)


response = urllib.request.urlopen('https://www.americanrhetoric.com/speeches/mlkihaveadream.htm')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
nuevo_texto= stop_words(text,'english')
freq = nltk.FreqDist(nuevo_texto)
print(freq.most_common(50))
freq.plot(20, cumulative=False)
