import requests
from bs4 import BeautifulSoup

page = requests.get('https://avatar.fandom.com/wiki/Transcript:The_Deserter')
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all('table')
print(tables)
print(tables[0].prettify())