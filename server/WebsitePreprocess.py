import csv
import nltk
import re
import mysql.connector
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class WebsitePreprocess:
    alpha_pattern = re.compile(r'[A-Za-z]+')
    stop_words = set(stopwords.words('english'))

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

    # Preprocess text
    def textCleaner(text) :
        words = word_tokenize(text)
        words = [word for word in words if alpha_pattern.match(word)]
        words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(words)

    # Grab website information
    def webParse(url) -> str:
        possible_author_class = [re.compile(r'.*(contributorname|contributor).*', re.IGNORECASE), re.compile(r'.*(author|author-?name).*', re.IGNORECASE), re.compile(r'.*(scriptwritername|writername|writer).*', re.IGNORECASE)]
        soup = BeautifulSoup(urlopen(url).read().decode("utf-8"), "html.parser")
        header = soup.find('h1')

        # TODO: Find way to get body using class elements in html and regex for filtering.
        author = None
        for class_name in possible_author_class:
            author = soup.find(['span', 'div', 'p'], class_ = class_name, recursive = True)
            if author:
                break

        # Test for getting
        print("Title:", textCleaner(header.text), "\n")
        print("Author/s:", textCleaner(author.text), "\n")


    print("\nTest 1:")
    url = 'https://www.bbc.com/news/world-europe-67008199'
    webParse(url)

    print("Test 2:")
    url = 'https'
    webParse(url)