
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
            if name in quotes:
                quotes[name].append(speech)
            else:
                quotes[name] = [speech]

    print(quotes)
    # print(len(quotes.keys()))


a = extract(x[1])