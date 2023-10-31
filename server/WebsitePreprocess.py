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
    alpha_pattern = re.compile(r'[A-Za-z]+')
    stop_words = set(stopwords.words('english'))

    # Preprocess text
    def textCleaner(text):
        words = word_tokenize(text)
        words = [word for word in words if WebsitePreprocess.alpha_pattern.match(word)]
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
            author = soup.find(['span', 'div', 'a', 'p'], class_ = refs, recursive = True)
            if author:
                author = WebsitePreprocess.textCleaner(author.text)
                break
            else:
                author = author = soup.find(['span', 'div', 'p', 'a'], id = refs, recursive = True)
                if author:
                    author = WebsitePreprocess.textCleaner(author.text)
                    break
                else:
                    author = 'No author found'
                    break

        # Test for getting
        print("Title:", header, "\n")
        print("Author/s:", author)

print("\nTest 1:")
url = 'https://www.bbc.com/news/world-europe-67008199'
WebsitePreprocess.parse(url)

print("\nTest 2:")
url = 'https://www.manilatimes.net/2022/05/30/news/comelec-shuts-down-automated-poll-system/1845514'
WebsitePreprocess.parse(url)

print("\nTest 3:")
url = 'https://newsinfo.inquirer.net/1840141/grade-5-pupil-dies-11-days-after-teacher-slapped-him-in-antipolo-city'
WebsitePreprocess.parse(url)

print("\nTest 4:")
url = 'https://edition.cnn.com/2023/10/02/americas/un-approves-haiti-military-mission-intl/index.html'
WebsitePreprocess.parse(url)

print("\nTest 5:")
url = 'https://edition.cnn.com/2023/10/03/asia/philippines-south-china-sea-scarborough-shoal-fishermen-dead-intl-hnk/index.html'
WebsitePreprocess.parse(url)

print()