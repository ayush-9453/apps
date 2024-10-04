import requests 
from bs4 import BeautifulSoup

def FetchAndSave(url, path):
    r = requests.get(url)
    with open(path, "w") as f :
        f.write(r.text)

url = "https://www.moneycontrol.com/promo/mc_interstitial_dfp.php?size=1280x540"

FetchAndSave(url,"WebScraping/data/money.html")

with open("WebScraping/data/money.html",'r') as g:
    html_doc = g.read()
    
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title)