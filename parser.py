from bs4 import BeautifulSoup
import requests
import sqlite3


url = 'http://nmt.edu.ru/html/cg.htm'
request = requests.get(url)
request.encoding = "utf-8"
soup = BeautifulSoup(request.text, 'html.parser')
group = soup.find_all("td", class_="ur")

with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS groups(id INTEGER, name TEXT, link TEXT) """)

id_counter = 0

for groups in group:
    groups = groups.find("a", {'class': 'z0'})
    if groups is not None:
        sublink = groups.get('href')
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO 'groups' (id, name, link) VALUES (?, ?, ?) """, (id_counter, groups.text, sublink))
        id_counter += 1