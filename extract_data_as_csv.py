from bs4 import BeautifulSoup
import requests
import json
import re
import csv

url = "https://roar.media/bangla/main/history-bn"

base_url = "https://roar.media/bangla/main/history/"

html_content = requests.get(url).text

header = ['Title', 'Author', 'Category', 'Source', 'Content']

soup = BeautifulSoup(html_content, "html.parser")

all_links = open('sport_link.json')
data = json.load(all_links)
# print(data)


title = ""
author = ""
content = ""
arti = ""

formated_text = []



for link in data:
    # print("link",link)
    if link.find(base_url) != -1:
      
        html_content_art = requests.get(link).text
        # print(html_content_art)
        soup_art = BeautifulSoup(html_content_art, "html.parser")
        check_head = soup_art.find("h1", class_="entry-title")
        if check_head is not None:
            title = soup_art.find("h1", class_="entry-title").get_text()
            print(title)

        check_author = soup_art.find("a", class_="post-author")
        if check_author is not None:
            author = soup_art.find("a", class_="post-author").get_text()
            print(author)

        # check_article_exists = soup_art.find('postcontentroarcheck')
        check_article_exists = soup_art.find('div', class_="entry-content")
        print(check_article_exists)
        
        if check_article_exists is not None:
            arti = soup_art.find('div', class_="entry-content")

            # arti = soup_art.find('postcontentroarcheck')
            # arti = soup_art.find_next_siblings(p)
            content = arti.get_text().strip()

        for art in arti:
            # print(art.get_text().strip())
            temp_arr = []
            formated_text.append(title)
            formated_text.append(author)
            formated_text.append("Science")
            formated_text.append(link)
            formated_text.append(content)
            # print('ff',formated_text)
            temp_arr.append(formated_text)
            
        # print(temp_arr)
        # temp_arr.append(formated_text)
        with open("history.csv", "w" ,encoding='UTF8') as f:
            history = csv.writer(f)
            history.writerow(header)
            history.writerow(temp_arr)
