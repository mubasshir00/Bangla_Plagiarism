from bs4 import BeautifulSoup
import requests
import json
import re

url = "https://roar.media/bangla/main/history-bn"

base_url = "https://roar.media/bangla/main/history/"

html_content = requests.get(url).text


soup = BeautifulSoup(html_content, "html.parser")

all_links = open('sport_link.json')
data = json.load(all_links)
# print(data)
formated_text = []

title = ""
author = ""
content = ""
arti = ""


for link in data:
    # print("link",link)
    if link.find(base_url) != -1:
        print(link)
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
            formated_text.append({
                "Title": title,
                "Author": author,
                "Category": "Science",
                "Source": link,
                "Content": content
            })
        print(formated_text)
        with open("sport2.json", "w") as f:
            f.write(str(formated_text))
