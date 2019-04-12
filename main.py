"""This file will:
 - Download the data
 - run through the analyzers
 - save the data from the analyzers"""
from twitter_analysis import get_tweets
from keras.models import Sequential
import csv
from keras.layers import Dense, Embedding, GlobalAveragePooling1D, Dropout
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
"""
poli_username = [
    # "realDonaldTrump",
    #                  "SecPompeo",
    #                  "MarkWarner",
    #                  "timkaine",
    #                  "ChrisVanHollen",
    #                  "SenatorCardin",
    "SenFeinstein",
    "KamalaHarris",
    "RepFredUpton",
    "Repjimbanks",
]  # List of politition usernames
sci_username = [
    # "zenbrainest",
    #                 "K_dele",
    #                 "betenoire1",
    #                 "doc2r06",
    #                 "sebatlab",
    "anne_churchland",
    "kaymtye",
    "alfairhall",
    "bita137",
    "CarolynBertozzi"
]  # List of scientists usernames

poli_text = []  # The texts from politions
sci_text = []  # The texts from scientists

job_usernames = [poli_username, sci_username]

# Get tweets
for job in job_usernames:
    for username in job:
        print("Getting text for " + username)
        # Download 30 tweets from each username
        for tweet in get_tweets(username, tweets=30, retweets=False):
            if tweet.get("orginaluser") == username:
                if job == poli_username:
                    poli_text.append(tweet.get("text"))
                elif job == sci_username:
                    sci_text.append(tweet.get("text"))

job_text = {"poli": poli_text, "sci": sci_text}
print("Done Downloading data.")
print(job_text)

with open('test_data.csv', mode='w') as test_data:
    test_data_writer = csv.writer(test_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for text in job_text["poli"]:
        test_data_writer.writerow([text, "poli"])
    for text in job_text["sci"]:
        test_data_writer.writerow([text, "sci"])
"""
# PREPROCESS




train_data_source = 'train_data.csv'
test_data_source = 'test_data.csv'
train_df = pd.read_csv(train_data_source, header=None)
test_df = pd.read_csv(test_data_source, header=None)

# convert string to lower case
train_texts = train_df[0].values
train_texts = [s.lower() for s in train_texts]
test_texts = test_df[0].values
test_texts = [s.lower() for s in test_texts]
# =======================Convert string to index================


# Tokenizer
tk = Tokenizer(num_words=None, char_level=True, oov_token='UNK')
tk.fit_on_texts(train_texts)
# If we already have a character list, then replace the tk.word_index
# If not, just skip below part
# -----------------------Skip part start--------------------------
# construct a new vocabulary
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"/\\|_@#$%^&*~`+-=<>()[]{}"
char_dict = {}
for i, char in enumerate(alphabet):
    char_dict[char] = i + 1

# Use char_dict to replace the tk.word_index
tk.word_index = char_dict
# Add 'UNK' to the vocabulary
tk.word_index[tk.oov_token] = max(char_dict.values()) + 1
# -----------------------Skip part end----------------------------
# Convert string to index
train_sequences = tk.texts_to_sequences(train_texts)
test_texts = tk.texts_to_sequences(test_texts)
# Padding
train_data = pad_sequences(train_sequences, maxlen=280, padding='post')
test_data = pad_sequences(test_texts, maxlen=280, padding='post')
# Convert to numpy array
train_data = np.array(train_data)
test_data = np.array(test_data)
# =======================Get classes================
train_classes = train_df[1].values
train_class_list = [x - 1 for x in train_classes]
test_classes = test_df[1].values
test_class_list = [x - 1 for x in test_classes]


# train_classes = to_categorical(train_class_list)
# test_classes = to_categorical(test_class_list)
print(train_classes, train_data)
print(test_classes, test_data)
# Build model

model = Sequential()
model.add(Embedding(10000, 16))
model.add(GlobalAveragePooling1D())
model.add(Dense(units=16, activation='relu'))
model.add(Dense(units=16, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Test model
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

print("Train model")
model.fit(train_data, train_classes, epochs=30, batch_size=64)

print("Testing model")
loss_and_metrics = model.evaluate(test_data, test_classes)
print("Results:")
print(loss_and_metrics)
