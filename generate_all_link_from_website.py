from bs4 import BeautifulSoup
import requests
import json
import re
import pandas as pd


url = "https://roar.media/bangla/main/history-bn"

base_url = "https://roar.media/bangla/main/history-bn"

html_content = requests.get(url).text


soup = BeautifulSoup(html_content, "html.parser")


p = soup.find_all('a')
all_links = []

for i in range(0, p.__len__()):
    for tag in p:
        data = {}
        data["links"] = tag.get('href')
        all_links.append(tag.get('href'))

with open("sport_link.json", "w") as f:
    f.write(json.dumps(all_links))
