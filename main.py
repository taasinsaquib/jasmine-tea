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
            name = line.find_all('th')[0].getText()
            # directions = line.find_all('i')[0].getText()
            speech = line.find_all('td')[0].getText()
            name = name.replace('\n', '')
            speech = speech.replace('[', '')
            speech = speech.replace(']', '')
            if name in quotes:
                quotes[name].append(speech)
            else:
                quotes[name] = [speech]
            # if directions in speech:
                # quotes[name].remove(directions)
    return(quotes)


def textGen(name, quote):
    text = ''
    for words in quote[name]:
        text += words
    text = text.rstrip('\r\n')
    return(text)
    
def create_file(name, quote):
    f = open(name+'.txt', 'a', encoding="utf-8")
    if name in quote:
        for line in quote[name]:
            f.write(line)
        f.close()


for transcript in transcript_titles:
    x = getsoup('https://avatar.fandom.com/wiki/'+transcript)
    for i in range(len(x)):
        quote = extract(x[i])
        name = "Suki"
        create_file(name,quote)

