"""This analyzer takes all the words, then averages the how long each word is"""

import textblob


class LengthOfWordsAnalyzer:
    def __init__(self, text, job):
        self.text = text
        self.job = job
        self.text_list = textblob.TextBlob(self.text).words
        self.average_len: int

    def _count_letters(self, word):
        return len(word)

    def average_list(self, list):
        sum_of_letters = sum(list)
        num_of_letters = len(list)
        return sum_of_letters/num_of_letters

    def count_letters(self):
        length_list = []
        for word in self.text_list:
            word_length = self._count_letters(word)
            length_list.append(word_length)
        return self.average_list(length_list)

    def process(self):
        """Return the tags"""
        return self.count_letters(), self.job
