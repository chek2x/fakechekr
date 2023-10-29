import csv
import re
import mysql.connector
from urllib.request import urlopen
from bs4 import BeautifulSoup

# # Connect to MySQL Local Server
# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "NewPassword"
# )

# tableCreation = ""

# # Navigate local server
# cursor = db.cursor()
# cursor.execute("CREATE TABLE")

# # Drop connection to MySQL
# db.close()

# url = 'https://www.bbc.com/news/world-europe-67008199'
 
# soup = BeautifulSoup(urlopen(url), features="lxml")
# header = soup.find('h1')

# print("Title of the article is : ")
# print (header.text)

# Grab website information
def webParse(url) -> str:
    soup = BeautifulSoup(urlopen(url).read().decode("utf-8"), "html.parser")
    header = soup.find('h1')

    # TODO: Find way to get body using class elements in html and regex for filtering.
    author = soup.find_all('div', attrs={'class' : re.compile(r'.*contributor.*')}, recursive = True)

    print("\nTitle:", header.text, "\n")
    print("Author/s:", author, "\n")

url = 'https://www.bbc.com/news/world-europe-67008199'
webParse(url)