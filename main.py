import pandas as pd
import pprint
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')
nltk.download('stopwords')

drake = pd.read_csv('drake/drake_data.csv')
take_care = {}  # empty dictionary which will hold track name and lyrics

# This code iterates through the rows of the DataFrame and constructs the take care dictionary with track names as
# keys and their corresponding lyrics as values.
for index, row in drake.iterrows():
    if row['album'] == 'Take Care':
        track = row['lyrics_title']
        lyrics = row['lyrics']
        take_care[track] = lyrics

# Convert all text to lowercase. This ensures that words like "love" and "Love" are treated as the same word during
# analysis.
for track, lyrics in take_care.items():
    new_lyrics = lyrics.lower()
    take_care[track] = new_lyrics

# Tokenization is the process of splitting text into individual words or phrases (tokens). In Python, you can use
# libraries like NLTK (Natural Language Toolkit) or spaCy to tokenize the lyrics.
for track, lyrics in take_care.items():
    tokens = word_tokenize(lyrics)
    take_care[track] = tokens

# Remove punctuation and stopwords
for track, lyrics in take_care.items():
    tokens = [word for word in lyrics if word.isalpha()]
    tokens = [word for word in lyrics if word not in stopwords.words('english')]

    take_care[track] = tokens

# Joining the cleaned tokens back into a text string
for track, lyrics in take_care.items():
    cleaned_lyrics = ' '.join(lyrics)
    take_care[track] = cleaned_lyrics

pprint.pprint(take_care)
