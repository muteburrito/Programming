# Step 1 - Import the important libraries 
from bs4.element import Comment, NavigableString
import requests
from bs4 import BeautifulSoup

# Step 2 - Get a URL for the HTML
url = "https://stackoverflow.com/"

r = requests.get(url)

htmlContent = r.content
# print(htmlContent)

# Step 3 - Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 4 - HTML Tree Traversal
title = soup.title # Title of HTML page
# print(title.string)

# Types of objects in bs:
# 1. Tag -  print(type(soup.title))
# 2. NavigableString - print(type(soup.title.string))
# 3. BS object - print(type(soup))
# 4. Comment

# Get all the paragraphs of the page
paras = soup.find_all('p')
#print(paras)

# Get all anchor tags
anchor = soup.find_all('a')
#print(anchor)
#print(soup.find_all('a'))  another way to find and print simultaneously 

# print(soup.find('p')) # This will return only the first paragraph tag 

#Get First element by using class
# print(soup.find('p')['class'])

# Getting a result using class
# print(soup.find_all('div', class_ = ('flush-left')))

# Print Text from tags 
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the links from anchor tag
all_links = set()
for link in anchor:
    if(link != '#'):
        all_links.add("https://stackoverflow.com/"+link.get('href'))