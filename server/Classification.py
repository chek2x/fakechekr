from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
import sqlite3
import pandas as pd
import numpy as np

class NaiveBayes:
    def classify(self, information: dict) -> str:
        # Connect to MySQL Database
        conn = sqlite3.connect('db_fakechekr.db')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")

        # Make data frame using pandas library with data from db
        data = pd.DataFrame(
            cursor.fetchall(),
            columns = [
                'article_id',
                'link',
                'website',
                'headline',
                'authors',
                'body',
                'pub_date',
                'legit'
            ]
        )
        cursor.close()

        data['legit'] = data['legit'].str.rstrip('\r')
        data['combined_text'] = data['link'] + " " + data['website'] + " " + data['headline'] + ' ' + data['authors'] + ' ' + data['body'] + ' ' +  + data['pub_date']

        # X represents features used for GaussianNB classifying of target label
        X_data = TfidfVectorizer().fit_transform(data['combined_text'].values)
        feature_names = TfidfVectorizer().fit(data['combined_text'].values).get_feature_names_out()
        # Y represents target label to predict
        Y_data = data['legit'].values

        X_train, X_test, Y_train, Y_test = train_test_split(X_data.toarray(), Y_data, test_size = 0.5, random_state = 5)
        gnb = GaussianNB()
        gnb.fit(X_train, Y_train)

        # Features to reference
        link = information['link']
        website = information['website']
        headline = information['headline']
        author = information['author']
        body = information['body']
        pub_date = information['pub_date']
        test_data = link + " " + website + " " + headline + " " + author + " " + body + " " + pub_date
        test_data = pd.DataFrame([test_data], columns = ['test_data'])
        test_data_vectorized = TfidfVectorizer(vocabulary=feature_names).fit_transform(test_data['test_data'].values)
        Y_pred = gnb.predict(test_data_vectorized.toarray())

        return Y_pred[0]
    
    def algoInfo():
        # Connect to MySQL Database
        conn = sqlite3.connect('db_fakechekr.db')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")

        # Make data frame using pandas library with data from db
        data = pd.DataFrame(
            cursor.fetchall(),
            columns = [
                'article_id',
                'link',
                'website',
                'headline',
                'authors',
                'body',
                'pub_date',
                'legit'
            ]
        )
        cursor.close()

        data['legit'] = data['legit'].str.rstrip('\r')
        data['combined_text'] = data['link'] + " " + data['website'] + " " + data['headline'] + ' ' + data['authors'] + ' ' + data['body'] + ' ' +  + data['pub_date']

        # X represents features used for GaussianNB classifying of target label
        X_data = TfidfVectorizer().fit_transform(data['combined_text'].values)
        # Y represents target label to predict
        Y_data = data['legit'].values

        X_train, X_test, Y_train, Y_test = train_test_split(X_data.toarray(), Y_data, test_size = 0.5, random_state = 5)
        gnb = GaussianNB()
        gnb.fit(X_train, Y_train)
        Y_pred = gnb.predict(X_test)

        # Test Outputs
        print("Accuracy:", accuracy_score(Y_test, Y_pred))
        print("Classification Report:\n", classification_report(Y_test, Y_pred))
        print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))