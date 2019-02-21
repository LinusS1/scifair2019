"""This file will:
 - Download the data
 - run through the analyzers
 - save the data from the analyzers"""
from twitter_analysis import get_tweets
import pickle
from analyzers.misspelled_words_analyzer import MisspellingsAnalyzer
from analyzers.length_of_words_analyzer import LengthOfWordsAnalyzer
from analyzers.negitive_words import NegativeScore
from analyzers.type_of_words_analyzer import WordTypesAnalyzer
from analyzers.word_case_analyzer import CapsScore

poli_username = []  # List of politition usernames
news_username = []  # List of reporters usernames
sci_username = ["SeaPubSchools"]  # List of scientists usernames

poli_text = []  # The texts from politions
news_text = []  # The texts from reporters
sci_text = []  # The texts from scientists

job_usernames = [poli_username, news_username, sci_username]

# Get tweets
for job in job_usernames:
    for username in job:
        print("Getting text for " + username)
        # Download 30 tweets from each username
        for tweet in get_tweets(username, tweets=30, retweets=False):
            if tweet.get("orginaluser") == username:
                if job == poli_username:
                    poli_text.append(tweet.get("text"))
                elif job == news_username:
                    news_text.append(tweet.get("text"))
                elif job == sci_username:
                    sci_text.append(tweet.get("text"))

job_text = {"poli": poli_text, "news": news_text, "sci": sci_text}
print("Done Downloading data.")
print("Running through analyzers")

################################
#  Run text through analyzers  #
################################

poli_analyzed = []
news_analyzed = []
sci_analyzed = []

for job, texts in job_text.items():
    for text in texts:
        misspelled_words = MisspellingsAnalyzer(text, job).process()
        length_of_words = LengthOfWordsAnalyzer(text, job).process()
        negative_score = NegativeScore(text, job).process()
        word_types = WordTypesAnalyzer(text, job).process()
        word_case = CapsScore(text, job).process()
        analyzed = {"misspelled_words": misspelled_words, "length_of_words": length_of_words,
                    "negative_score": negative_score, "word_types": word_types, "word_case": word_case}
        if job == "poli":
            poli_analyzed.append(analyzed)
        elif job == "news":
            news_analyzed.append(analyzed)
        elif job == "sci":
            sci_analyzed.append(analyzed)

with open('poli.pickle', 'wb') as handle:
    pickle.dump(poli_analyzed, handle)
with open('news.pickle', 'wb') as handle:
    pickle.dump(news_analyzed, handle)
with open('sci.pickle', 'wb') as handle:
    pickle.dump(sci_analyzed, handle)

print(sci_analyzed)
