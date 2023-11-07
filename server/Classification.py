from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
import mysql.connector
import pandas as pd
import numpy as np

# Connect to MySQL Database
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "NewPassword",
    database = "db_fakechekr"
)

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
data['combined_text'] = data['link'] + " " + data['headline'] + ' ' + data['authors'] + ' ' + data['body'] + ' ' +  + data['pub_date'].apply(lambda x: x.strftime('%Y-%m-%d'))

# X represents features used for GaussianNB classifying of target label
X_data = TfidfVectorizer().fit_transform(data['combined_text'].values)
feature_names = TfidfVectorizer().fit(data['combined_text'].values).get_feature_names_out()
# Y represents target label to predict
Y_data = data['legit'].values

X_train, X_test, Y_train, Y_test = train_test_split(X_data.toarray(), Y_data, test_size = 0.5, random_state = 5)
gnb = GaussianNB()
# gnb.fit(X.toarray(), Y)
gnb.fit(X_train, Y_train)
# Y_pred = gnb.predict(X_test)

# Sample Test
link = "http://fakenewsarticle.com/a-bunch-of-stuff"
website = "Lorem Ipsum"
headline = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sollicitudin, nibh quis viverra ultrices, felis quam porttitor dui, nec posuere tortor enim sit amet lacus. Morbi placerat turpis at volutpat vestibulum."
author = "John Doe"
body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc auctor sollicitudin mi, quis varius nisi semper in. Duis vel lorem dui. In facilisis quam et leo lobortis, non eleifend urna malesuada. Sed efficitur dapibus eros. In fringilla vitae ipsum at auctor. Nunc placerat lorem mauris, eu tincidunt tellus cursus vitae. In eget nunc nunc. Sed sit amet faucibus sapien. Sed tristique mi quis diam viverra, ac suscipit mi rhoncus. Phasellus at lectus eu risus sodales posuere eget et purus. Donec nunc neque, vulputate eget interdum sed, tincidunt eu libero. Fusce et laoreet ipsum. Nulla pulvinar, mi sit amet ullamcorper molestie, ligula arcu facilisis enim, eget viverra neque dolor in magna. Ut id viverra velit, quis blandit ipsum. Etiam quis quam magna. Sed at est felis. Proin vestibulum, risus id luctus aliquam, mi quam tempor eros, sit amet venenatis turpis magna sed nisl. Duis tristique nunc orci, placerat gravida massa commodo in. Phasellus congue interdum turpis et venenatis. Suspendisse lacus est, suscipit sit amet egestas a, ultricies at massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque eu accumsan ipsum, vel vehicula magna. Quisque sagittis, nunc et luctus faucibus, sapien nunc laoreet neque, cursus ornare urna quam at est. Vestibulum blandit lacus ac consequat finibus. Donec ut diam velit. Nulla elementum metus id euismod lobortis. Proin finibus libero quam, non ultrices nibh viverra ut. Nullam ac accumsan nibh, vitae feugiat eros. Phasellus vestibulum diam eu metus mattis placerat. Vivamus condimentum tellus orci, nec eleifend est faucibus eu. Nunc semper neque in lectus facilisis efficitur. Donec mattis bibendum tempor. Integer vel felis id quam ultricies convallis ut ut nibh. Aenean rutrum odio ac ante vehicula, et eleifend elit suscipit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed nec orci volutpat, maximus mauris quis, aliquam mauris. Duis sollicitudin ultrices consequat. Donec consectetur justo a quam maximus tempus nec a sem. Etiam lacinia ac massa sed gravida. Nulla nec euismod quam, at accumsan mi. Aenean volutpat semper dolor sit amet dignissim. Phasellus bibendum enim eget nunc vulputate aliquam in in lectus. Vestibulum viverra arcu vitae purus elementum accumsan. Sed scelerisque scelerisque purus ac porta. Nulla elementum elementum tellus, sit amet pretium diam mollis nec. Cras lectus quam, gravida eget congue vel, porta nec neque. Nullam fermentum, erat vitae interdum aliquet, nisl lacus mollis eros, in consequat lectus ante vitae nibh. Fusce ut dignissim enim. In ac lorem tellus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent lacus mauris, placerat quis placerat non, hendrerit tincidunt eros. Quisque lobortis pulvinar fermentum."
pub_date = "0001-01-01"
test_data = link + " " + website + " " + headline + " " + author + " " + body + " " + pub_date
test_data = pd.DataFrame([test_data], columns = ['test_data'])
test_data_vectorized = TfidfVectorizer(vocabulary=feature_names).fit_transform(test_data['test_data'].values)
Y_pred = gnb.predict(test_data_vectorized.toarray())

print(Y_pred)

# Test Outputs
# print("Accuracy:", accuracy_score(Y_test, Y_pred))
# print("Classification Report:\n", classification_report(Y_test, Y_pred))
# print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))

# pd.set_option('display.max_columns', None)
# print(data['legit'])
# print(X_test)