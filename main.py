import markovify
import requests
from bs4 import BeautifulSoup


def getsoup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    tables = soup.find_all('table', {"class": "wikitable"})

    return tables


x = getsoup('https://avatar.fandom.com/wiki/Transcript:The_Last_Airbender')


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

    #print(quotes)
    return(quotes)
    # print(len(quotes.keys()))

def textGen(name, quote):
    text = ''
    for words in quote[name]:
        text += words
    text = text.rstrip('\r\n')
    print(text)
    text_model = markovify.Text(text)
    for i in range(3):
        print(text_model.make_sentence())
    

a = extract(x[1])
keyIn = 'Iroh'
print(a.keys())
b = textGen(keyIn, a)