"""This analyzes text for how many letters are Capitatlized.
First, the program counts how many letters are capitalized.
Then it counts how many letters there are in the text.
Finally, it finds the "Capitalization score" by dividing the number of capitalized letters by
the number of letters in the text
"""
import string
import re


class CapsScore:
    def __init__(self, text, job):
        self.text = text
        self.job = job

    @property
    def pre_process(self):
        """Take out spaces and punctuation"""
        return re.sub(r'[^\w\s]','',self.text.replace(" ", ""))

    def count_num_caps(self):
        """Count number of letters that are capitalized"""
        text = self.pre_process
        return sum(1 for c in text if c.isupper())

    def count_num_letters(self):
        return len(self.pre_process)

    def score(self):
        caps = self.count_num_caps()
        letters = self.count_num_letters()
        score = caps/letters
        return score

    def process(self):
        return self.score(), self.job
