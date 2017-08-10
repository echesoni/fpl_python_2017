import pandas as pd
import bs4
from bs4 import BeautifulSoup
import requests
import html5lib

player_dict = {}

url = 'https://www.dreamteamfc.com/statistics/players/ALL/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html5lib')

name_list = []

for td in soup.findAll("td", {"class" : "tabName"}):
    name = td.text.split('Statistics')[-1].strip()
    if name:
        name_list.append(name)
        res = [i.text for i in td.next_siblings if isinstance(i, bs4.element.Tag)]
        position, team, vfm, value, points = res
        value = value.strip('m')
        player_dict[name] = [name, position, team, vfm, value, points]
print('Found: %s' % len(name_list))
print(name_list[-1])