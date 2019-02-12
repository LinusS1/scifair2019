"""This analyzes text for how many letters are Capitatlized.
First, the program counts how many letters are capitalized.
Then it counts how many letters there are in the text.
Finally, it finds the "Capitalization score" by dividing the number of capitalized letters by
the number of letters in the text
"""


class CapsScore:
    def __init__(self, text):
        self.text = text

    def pre_process(self):
        """Take out spaces"""
        return self.text.replace(" ", "")

    def count_num_caps(self):
        """Count number of letters that are capitalized"""
        text = self.pre_process()
        return sum(1 for c in text if c.isupper())

    def count_num_letters(self):
        return len(self.pre_process())

    def score(self):
        caps = self.count_num_caps()
        letters = self.count_num_letters()
        score = caps/letters
        return score

    def process(self):
        return self.score()

