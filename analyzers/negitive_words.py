"""Find how many negative words there are in a sentence.
This uses a preconfigured negative words file, which lists thousands of negative words.
The input text is given a negativity score: number of negative divided by total number of words.
"""

import re

# Load all the negative words
neg_sent = open("negative_words.txt").read()
negative_words=neg_sent.split('\n')
negative_counts=[]

class NegativeScore:
    def __init__(self, text, job):
        self.text = text
        self.job = job

    def pre_process(self):
        """Take out spaces and punctuation"""
        return re.sub(r'[^\w\s]','',self.text.lower()).split(' ')

    def count_num_negative_words(self):
        """Count number of letters that are capitalized"""
        negative_word_count = 0
        text = self.pre_process()
        for word in text:
            if word in negative_words:
                negative_word_count += 1
        return negative_word_count

    def count_num_words(self):
        return len(self.pre_process())

    def score(self):
        neg_words = self.count_num_negative_words()
        words = self.count_num_words()
        score = neg_words/words
        return score

    def process(self):
        return self.score(), self.job
