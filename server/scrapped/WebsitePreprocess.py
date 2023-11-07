import csv
import nltk
import re
import mysql.connector
import urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# TODO: Find a way to use information for GaussianNB classification
class WebsitePreprocess:
    alphanumeric_pattern = re.compile(r'[A-Za-z0-9]+')
    stop_words = set(stopwords.words('english'))

    # Preprocess text
    def textCleaner(text):
        words = word_tokenize(text)
        words = [word for word in words if WebsitePreprocess.alphanumeric_pattern.match(word)]
        words = [word for word in words if word.lower() not in WebsitePreprocess.stop_words]
        return ' '.join(words)

    # Grab website information
    def parse(url):
        possible_author_refs = [
            re.compile(r'.*contributornames?.*', re.IGNORECASE),
            re.compile(r'.*contributors?.*', re.IGNORECASE),
            re.compile(r'.*authors?.*', re.IGNORECASE),
            re.compile(r'.*author-?names?.*', re.IGNORECASE),
            re.compile(r'.*scriptwriternames?.*', re.IGNORECASE),
            re.compile(r'.*writernames?.*', re.IGNORECASE),
            re.compile(r'.*writers?.*', re.IGNORECASE),
            re.compile(r'.*names?.*', re.IGNORECASE)
        ]
        
        # TODO: Handle exception better
        try:
            soup = BeautifulSoup(urlopen(url).read().decode("utf-8"), "html.parser")
        except urllib.error.HTTPError as e:
            print('Error with web scraping.', e)
            return

        # Find article title
        header = soup.find('h1')
        if header:
            header = WebsitePreprocess.textCleaner(header.text)
        else:
            header = "No title found"

        # Find article author/s
        for refs in possible_author_refs:
            author = soup.find(['div', 'span', 'a', 'p'], class_ = refs, recursive = True)
            if author:
                author = WebsitePreprocess.textCleaner(author.text)
                author_text = ' '.join([word for word in author_text.split() if word.lower() != 'cnn'])
                break
            
            else:
                author = soup.find(['div', 'span', 'a', 'p'], id = refs, recursive = True)
                if author:
                    author = WebsitePreprocess.textCleaner(author.text)
                    break
                else:
                    author = 'No author found'

        # Test for getting
        print("Title:", header, "\n")
        print("Author/s:", author)

url = 'https://www.bbc.com/news/world-europe-67008199'
print("\nTest 1: (" + url + ")")
WebsitePreprocess.parse(url)

url = 'https://edition.cnn.com/2023/10/02/americas/un-approves-haiti-military-mission-intl/index.html'
print("\nTest 2: (" + url + ")")
WebsitePreprocess.parse(url)

print()