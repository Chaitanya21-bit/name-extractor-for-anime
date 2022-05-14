from bs4 import BeautifulSoup
import requests
import re

url = "https://w13.mangafreak.net/"
result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

# print(doc.prettify())

m_list = doc.find_all(class_="latest_item")
print(m_list[0].find())

main_list = []

for i in range(len(m_list)):
    name = m_list[i].find(class_="name").string
    # print(name)
    main_list.append(name)

    # image = m_list[i].find(class_="image")
    # print(m_list[i].get('src'))

# print(main_list)
