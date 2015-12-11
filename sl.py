# coding=utf-8
import requests
from bs4 import BeautifulSoup

url = "http://www.mysoal.com/moments/9JjqHTN2OEvnFeXZO4uUGT8LLOx4I-xJZOlQeYp6Cs0"
page  = requests.get(url).text
soup = BeautifulSoup(page,"lxml")

tayara_listing = soup.find("div", class_="moment")
tayara_item = tayara_listing.find_all("div", class_="moment-content")

for tayara_title in tayara_item:
    tayara_info = tayara_title.find("div", class_="moment-image")
    print(tayara_info.img)
    tayara_msg = tayara_title.find("div", class_="moment-theme")
    print(tayara_msg.p)
    tayara_cap = tayara_title.find("div", class_="moment-caption")
    print(tayara_cap.p)
    tayara_audio = tayara_title.find("div", class_="moment-audio")
    print(tayara_audio.source)
