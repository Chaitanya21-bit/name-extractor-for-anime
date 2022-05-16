from bs4 import BeautifulSoup
import requests
import re


class My_manga_list:

    def __init__(self, link, number):
        self.url = link
        self.number = number

    def gen_name_list(self):
        main_list = []

        for i in range(0, self.number):
            name = mangas[i].find(class_="name").string

            main_list.append(name)

        return main_list

    def gen_img_list(self):
        img_list = []
        for i in range(0, self.number):
            image = mangas[i].find(class_="image").img

            img_list.append(image['src'])

        return img_list


def gen_dict(main_list, img_list):
    my_dict = dict(zip(main_list, img_list))
    return my_dict


url = "https://w13.mangafreak.net/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
mangas = doc.find_all(class_="latest_item")

num = int(input("No. of manga u want:\n"))
obj = My_manga_list(url, num)
m_list = obj.gen_name_list()
m_img = obj.gen_img_list()
m_dict = gen_dict(m_list, m_img)
print(m_list)
print(m_img)
print(m_dict)
