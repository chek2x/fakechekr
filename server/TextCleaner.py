import re
import string

class TextCleaner:
    def clean_text(self, input_text):
        # Convert text to lowercase
        lowercase_text = input_text.lower()
        
        # Remove punctuation using regular expressions
        no_punctuation_text = re.sub(f"[{re.escape(string.punctuation)}]", "", lowercase_text)
        
        # Replace multiple spaces with a single space
        cleaned_text = re.sub(r"\s+", " ", no_punctuation_text).strip()
        
        return cleaned_text