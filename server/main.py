from Classification import NaiveBayes
from TextCleaner import TextCleaner
import pyscript
import sqlite3

# Connect to MySQL Database
conn = sqlite3.connect('db_fakechekr.db')
cursor = conn.cursor()

# Initiate NaiveBayes local class
nb = NaiveBayes()

form_values = {
    "link" : "",
    "website" : "",
    "headline" : "none",
    "author" : "none",
    "body" : "none",
    "pub_date" : "0001-01-01"
}

def submit_handler(event = None):
    if event:
        event.preventDefault()
        result = nb.classify(form_values)
        cursor.execute("INSERT INTO articles (link, website, headline, authors, body, pub_date, legit) VALUES (\""
               + form_values['link'] + "\", \""
               + form_values['website'] + "\", \""
               + form_values['headline'] + "\", \""
               + form_values['author'] + "\", \""
               + form_values['body'] + "\", \""
               + form_values['pub_date'] + "\", \""
               + result + "\")")
        conn.commit()
        display(f"Result: {result}", target = 'result_text')
    
def link_input_handler(event = None):
    if event:
        event.preventDefault()
        form_values['link'] = Element("link_search").element.value

def website_input_handler(event = None):
    if event:
        event.preventDefault()
        form_values['website'] = Element("link_search").element.value

def headline_input_handler(event = None):
    if event:
        event.preventDefault()
        form_values['headline'] = Element("headline_search").element.value

def author_input_handler(event = None):
    if event:
        event.preventDefault()
        form_values['author'] = Element("authors_search").element.value
        
def body_input_handler(event = None):
    if event:
        event.preventDefault()
        form_values['body'] = Element("body_search").element.value

def date_input_handler(event = None):
    if event:
        event.preventDefault()
        form_values['pub_date'] = Element("date_search").element.value

Element("link_search").element.oninput = link_input_handler
Element("website_search").element.oninput = website_input_handler
Element("headline_search").element.oninput = headline_input_handler
Element("authors_search").element.oninput = author_input_handler
Element("body_search").element.oninput = body_input_handler
Element("date_search").element.oninput = date_input_handler
Element("form").element.onsubmit = submit_handler