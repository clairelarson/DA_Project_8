from lib2to3.pgen2.pgen import DFAState
from key import api_key
from urllib import request, response
import requests
import csv
import pandas as pd
oscar = pd.read_csv("oscar_winners.csv")

#get data
L = oscar['IMDB'].tolist()

df = []

# function to create data
def req_data(list):
    for imdbid in list:
        res = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&i={imdbid}')
        data = res.json()
        title = data['Title']
        year = data['Year']
        rated = data['Rated']
        rt = data['Runtime']
        rt = rt.split(' ')
        runt = int(rt[0])
        genre = data['Genre']
        direct = data['Director']
        awards = data['Awards']
        awards = awards.split(" ")
        aWin = int(awards[3])
        aNom = int(awards[6])
        bx = data['BoxOffice']
        bx = bx.replace(',', '')
        bx = bx.split('$')
        box = int(bx[1])
        ls = [title, year, rated, runt, genre, direct, aWin, aNom, box]
        df.append(ls)
    return df

req_data(L)

# csv header
header = ['Movie Title', 'Year', 'Rated', 'Runtime', 'Genre', 'Director', 'Award Wins', 'Award Nominations', 'Box Office']

with open('movies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in df:
        writer.writerow(row)