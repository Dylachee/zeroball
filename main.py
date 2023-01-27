import csv

import requests 
from bs4 import BeautifulSoup 
from bs4.element import ResultSet, Tag 

URL = 'https://www.kivano.kg/mobilnye-telefony' 

response = requests.get(URL) 

html = response.text

soup = BeautifulSoup(html, 'html.parser') 

cards = soup.find_all('div', class_='item')  

result = [] 
for tag in cards: 
    title = tag.find('div', class_='listbox_title oh').text
    price = tag.find('div', class_='listbox_price').text 
    desc = tag.find('div', class_='product_text').text 
    img_link = tag.find('div', class_='listbox_img').find('img').get('src') 
    
    obj = { 
        'title': title.strip(), 
        'price': price.strip(),
        'description': desc.strip().replace('\n', ''),
        'image_link': img_link,
    }
    result.append(obj)


with open('smartphones.csv', 'w') as file: 
    names = ['title', 'price', 'description', 'image_link'] 
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader() 
    for notebook in result: 
        writer.writerow(notebook) 