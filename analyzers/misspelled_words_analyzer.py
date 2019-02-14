"""This analyzer looks through all the words, and counts how many are misspelled.
It then returns how many misspelled words divided by the number of total words."""

import textblob


class MisspellingsAnalyzer:
    def __init__(self, text, job):
        self.text = text
        self.job = job
        self.text_list_original = textblob.TextBlob(self.text)
        self.text_list_corrected = textblob.TextBlob(self.text)

    def correct_words(self):
        self.text_list_corrected = self.text_list_corrected.correct()
        return self.text_list_corrected

    def turn_to_list(self):
        self.text_list_corrected = self.text_list_corrected.words
        self.text_list_original = self.text_list_original.words

    def compare_lists(self, list1, list2):
        """Returns number of words changes"""
        changes = len(set(list1).intersection(list2))
        num_words = len(self.text_list_original)
        return num_words - changes

    def total_words(self):
        return len(textblob.TextBlob(self.text).words)

    def process(self):
        """Return the tags"""
        self.correct_words()
        self.turn_to_list()
        num_changed = self.compare_lists(self.text_list_original, self.text_list_corrected)
        return num_changed/self.total_words(), self.job

