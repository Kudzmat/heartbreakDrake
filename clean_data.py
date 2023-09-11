import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
import string
import pprint

nltk.download('punkt')
nltk.download('stopwords')

DRAKE_DATA = pd.read_csv('drake/drake_data.csv')


# Get album lyrics from user input
def get_album_lyrics():
    album_lyrics = []  # empty list will hold all the lyrics from an album by track
    for index, row in DRAKE_DATA.iterrows():
        if row['album'] == 'Take Care':
            lyrics = row['lyrics']
            album_lyrics.append(lyrics)
    return album_lyrics

# Processing th elyrics by cleaning the up
def process_lyrics(lyrics_list):
    processed = []
    for lyrics in lyrics_list:
        new_lyrics = lyrics.lower()
        tokens = word_tokenize(new_lyrics)
        # Remove punctuation and stopwords
        tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]
        processed.extend(tokens)  # Extend the list with the tokens
    return processed


def check_frequency(tokens):
    word_frequency = Counter(tokens)
    # Find the 10 most common words
    most_common_words = dict(word_frequency.most_common(20))

    # Print the most common words and their frequencies
    for word, num in most_common_words.items():
        print(f'{word}: {num}')


lyrics_list = get_album_lyrics()
clean_lyrics = process_lyrics(lyrics_list)

check_frequency(clean_lyrics)
