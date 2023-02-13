from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

title_infos = soup.find_all(name="h3", class_="title")

title = []
position = []
for info in title_infos:
    if ":" not in info.string[:4]:
        title.append(info.string.split(") ")[1])
        position.append(int(info.string.split(") ")[0]))
    else:
        title.append(info.string.split(": ")[1])
        position.append(int(info.string.split(": ")[0]))

with open("movies_to_watch.txt", mode="w", encoding='utf-8') as file:
    for pos in position:
        file.write(f"{position[pos-1]} - {title[pos-1]}\n")
