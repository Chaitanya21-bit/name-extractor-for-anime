from bs4 import BeautifulSoup
import requests
import re


url = "https://w13.mangafreak.net/"
result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

# print(doc.prettify())

mangas = doc.find_all(class_="latest_item")
# print(mangas)


main_list = []

for manga in mangas:
    name = manga.find(class_="name").string
    # print(name)
    main_list.append(name)

    image = manga.find(class_="image").img
    print(image['src'])


# print(main_list)
