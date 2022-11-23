from bs4 import BeautifulSoup
import requests
import json
import re


url = "https://roar.media/bangla/main/sports"

base_url = "https://roar.media/bangla/main/sports"

html_content = requests.get(url).text


soup = BeautifulSoup(html_content, "html.parser")


p = soup.find_all('a')

all_links = []

# for i in range(2, 3):
#     for tag in p:
#         # print(tag.get('href'))
#         all_links.append(tag.get('href'))

all_links_test = open('sport_link.json')
print(all_links_test)
data = json.load(all_links_test)
print(data)

formated_text = []

title = ""
author = ""
content = ""
arti = ""

for link in all_links:
    if link.find(base_url) != -1:
        html_content_art = requests.get(link).text

        soup_art = BeautifulSoup(html_content_art, "html.parser")

        check_head = soup_art.find("h1", class_="entry-title")
        if check_head is not None:
            title = soup_art.find("h1", class_="entry-title").get_text()

        check_author = soup_art.find("a", class_="post-author")
        if check_author is not None:
            author = soup_art.find("a", class_="post-author").get_text()

        check_article_exists = soup_art.find('postcontentroarcheck')
        if check_article_exists is not None:
            arti = soup_art.find('postcontentroarcheck')
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

        with open("sport2.json", "w") as f:
            f.write(str(formated_text))

        # with open('science.txt', 'w') as f:
        #     f.write(str(formated_text))
