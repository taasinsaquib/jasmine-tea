import markovify
import requests
from bs4 import BeautifulSoup

def getsoup_episodes(url):
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    episodes = soup.find_all("a", {"class": "category-page__member-link"})
    transcript_titles = [episode.string for episode in episodes]
    
    return transcript_titles

transcript_titles = getsoup_episodes('https://avatar.fandom.com/wiki/Category:Avatar:_The_Last_Airbender_episode_transcripts?oldid=1052211')

def getsoup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    tables = soup.find_all('table', {"class": "wikitable"})

    return tables

def extract(table):
    quotes = {}
    lines = table.find_all('tr')
    for line in lines:
        childTag = line.find('th')
        if childTag:
            name = line.find_all('th')[0].string
            speech = line.find_all('td')[0].string
            name = name.replace('\n', '')
            if name in quotes:
                quotes[name].append(speech)
            else:
                quotes[name] = [speech]
    return(quotes)


def textGen(name, quote):
    text = ''
    for words in quote[name]:
        text += words
    text = text.rstrip('\r\n')
    return(text)
    

for transcript in transcript_titles:
    x = getsoup('https://avatar.fandom.com/wiki/'+transcript)
    for i in range(len(x)):
        a = extract(x[i])
        keyIn = 'Iroh'
        print(a.keys())
        b = textGen(keyIn, a)

text_model = markovify.Text(text)
for i in range(3):
   print(text_model.make_sentence())
