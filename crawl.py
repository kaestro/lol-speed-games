from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.op.gg/champion/statistics")
bsObject = BeautifulSoup(html, "html.parser")

champions = bsObject.findAll('div', {"class": "champion-index__champion-item__name"})

for champion in champions:
    print(champion)
    print(type(champion))

