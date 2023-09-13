import pandas as pd
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
import string
import pprint

nltk.download('punkt')
nltk.download('stopwords')

DRAKE_DATA = pd.read_csv('drake/drake_data.csv')
TINASHE_DATA = pd.read_csv('tinashe/tinashe.csv')


# Get album lyrics from user input
def get_album_lyrics():
    album_lyrics = []  # empty list will hold all the lyrics from an album by track

    for index, row in TINASHE_DATA.iterrows():
        lyrics = row['lyrics']
        album_lyrics.append(lyrics)

    """"
    for index, row in DRAKE_DATA.iterrows():
        if row['album'] == 'Take Care':
            lyrics = row['lyrics']
            album_lyrics.append(lyrics)
    """
    return album_lyrics


# Processing the lyrics by cleaning the up
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
    lyrics_count = {}  # This dictionary will hold a word and the number of times it appears
    word_frequency = Counter(tokens)
    # Find the 10 most common words
    most_common_words = dict(word_frequency.most_common(50))

    # Print the most common words and their frequencies
    for word, num in most_common_words.items():
        lyrics_count[word] = num
        #print(f'{word}: {num}')

    return lyrics_count


def create_bar_graph(count_dict):
    words = list(count_dict.keys())
    appearances = list(count_dict.values())
    plt.figure(figsize=(15, 10))
    plt.bar(range(len(count_dict)), appearances, tick_label=words)
    plt.show()


lyrics_list = get_album_lyrics()
clean_lyrics = process_lyrics(lyrics_list)

word_count = check_frequency(clean_lyrics)
create_bar_graph(word_count)

