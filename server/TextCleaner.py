import re
import string
import nltk
from nltk.corpus import stopwords

class TextCleaner:
    def download_stopwords():
        if not nltk.data.find('corpora/stopwords.zip'):
            nltk.download('stopwords')

    def clean_text(input_text):
        TextCleaner.download_stopwords()

        # Convert text to lowercase
        lowercase_text = input_text.lower()
        
        # Remove punctuation using regular expressions
        no_punctuation_text = re.sub(f"[{re.escape(string.punctuation)}]", "", lowercase_text)
        
        # Replace multiple spaces with a single space
        cleaned_text = re.sub(r"\s+", " ", no_punctuation_text).strip()
        
        # Remove common stop words
        stop_words = set(stopwords.words('english'))
        words = cleaned_text.split()
        filtered_words = [word for word in words if word not in stop_words]
        cleaned_text = " ".join(filtered_words)
        
        return cleaned_text