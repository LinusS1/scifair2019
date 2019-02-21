"""This file will download the data"""
from twitter_analysis import get_tweets
import pickle

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
print(job_text)
# Store them with job
with open('text.pickle', 'wb') as handle:
    b = pickle.dump(job_text, handle)

