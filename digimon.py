# Web Scraping List of Digimon from wikimon.net and store them into dictionary typed database
from bs4 import BeautifulSoup
import requests

url = 'https://wikimon.net/Visual_List_of_Digimon'
x = requests.get(url)
y = BeautifulSoup(x.content, 'html.parser')

listDigimon = []

for i in y.find_all('img'):
    dictDigimon = {
        'name' : i.get('alt'),
        'pict' : 'https://wikimon.net/'+ i.get('src')
    }
    listDigimon.append(dictDigimon)


# write output from web scrapping into csv file
import csv

with open('listDigimon.csv', 'w', newline='', encoding='utf-8') as file_csv:
    header_csv = ['name', 'pict']
    writer = csv.DictWriter(file_csv, fieldnames = header_csv)
    writer.writeheader()
    for i in range(len(listDigimon)-2):
        writer.writerow(listDigimon[i])

# insert csv data into mysql database
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = '<yourUsername>',
    passwd = '<yourPassword>',
    database = 'digimon'
)

delete = mydb.cursor().execute('delete from digimon')          # delete the existing file so every time python file runs, it won't stack to the old one, instead overwrite it
start = mydb.cursor().execute('ALTER TABLE digimon AUTO_INCREMENT = 1')     # to set the id colum to start over from no 1

for i in range(len(listDigimon)-2):
    name = listDigimon[i]['name']
    pict = listDigimon[i]['pict']
    x = mydb.cursor()
    x.execute('insert into digimon (name,pict) values (%s, %s)', (name,pict))
    mydb.commit()
