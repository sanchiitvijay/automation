from bs4 import BeautifulSoup
import os
import pandas as pd

d = []

# name - KzDlHZ
# price - Nx9bqj
# link - CGtC98


for file in os.listdir("data"):

    with open(f"data/{file}","r", encoding="utf-8") as f:
      
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, "html.parser")
    try:
        n = soup.find('div', {'class':'KzDlHZ'}).get_text()
        pp = soup.find('div', {'class':'Nx9bqj'}).get_text()
        l = soup.find('a')
        ll = "https://flipkart.com/" + l.get('href')

        d.append({
            'title': n,
            'price': pp,
            'link': ll
        })

    except Exception as e:
        print(e)

df = pd.DataFrame(data = d)
df.to_csv("data.csv")