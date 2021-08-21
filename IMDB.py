# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 03:25:39 2020
@author: patricio.a.drasal
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

#title.ratings.tsv.gz – Contains the IMDb rating and votes information for titles
 #tconst (string) - alphanumeric unique identifier of the title
 #averageRating – weighted average of all the individual user ratings
 #numVotes - number of votes the title has received

ratings = pd.read_csv('Bases/title.ratings.tsv.gz', compression='gzip', header=0,sep='\t')
ratings

ratings.info()

#title.basics.tsv.gz
 #title.basics.tsv.gz - Contains the following information for titles:
 #tconst (string) - alphanumeric unique identifier of the title
 #titleType (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc)
 #primaryTitle (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
 #originalTitle (string) - original title, in the original language
 #isAdult (boolean) - 0: non-adult title; 1: adult title
 #startYear (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
 #endYear (YYYY) – TV Series end year. ‘\N’ for all other title types
 #runtimeMinutes – primary runtime of the title, in minutes
 #genres (string array) – includes up to three genres associated with the title


col_list = ["tconst", "titleType","primaryTitle","startYear","genres"]
titles = pd.read_csv('Bases/title.basics.tsv.gz', compression='gzip', header=0,sep='\t',usecols=col_list)

titles.info()
titles.head()
titles.describe()

titles.titleType.unique()

complete=(pd.merge(titles, ratings))

complete.columns
complete.head(2)
complete.info()
#Combining Datasets: Merge and Join

movies=complete.query("titleType == 'movie'")

#or
top=movies[(movies.numVotes > 100000) & (movies.averageRating > 8)].sort_values(["averageRating","numVotes"] ,ascending=[False,True])
                                                                  
series=complete.query("titleType == 'tvSeries'")
top_series= series[(series.numVotes > 100000) & (series.averageRating > 8)].sort_values(["averageRating","numVotes"] ,ascending=[False,False]) 
series