"""This analyzer looks at all the words and returns how many of a type of word there is
The dog ran -> One noun and One verb

The program loops through the words and decides what type they are.
Then, it returns how many of the type of word there is.
"""
from textblob import TextBlob


class WordTypesAnalyzer:
    def __init__(self, text):
        self.text = text
        self.text_blob = TextBlob(self.text)

    def process(self):
        """Return the tags"""
        return self.text_blob.tags

