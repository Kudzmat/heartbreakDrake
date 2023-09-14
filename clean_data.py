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


nltk.download('punkt')
nltk.download('stopwords')

DRAKE_DATA = pd.read_csv('drake/drake_data.csv')
TINASHE_DATA = pd.read_csv('tinashe/tinashe.csv')
ALBUM = 'Take Care'


# Get album lyrics from user input
def get_album_lyrics():
    album_lyrics = []  # empty list will hold all the lyrics from an album by track

    for index, row in DRAKE_DATA.iterrows():
        if row['album'] == ALBUM:
            lyrics = row['lyrics']
            album_lyrics.append(lyrics)

    return album_lyrics


# Processing the lyrics by cleaning the up
def process_lyrics(lyrics_list):
    processed = []
    custom_stopwords = ['yeah', 'oh', 'nigga', 'chorus', 'Drake', 'drake', 'niggas']
    for lyrics in lyrics_list:
        new_lyrics = lyrics.lower()
        tokens = word_tokenize(new_lyrics)
        # Remove punctuation and stopwords (both English and custom)
        tokens = [word for word in tokens if word.isalpha() and word.lower() not in stopwords.words(
            'english') and word.lower() not in custom_stopwords]
        processed.extend(tokens)  # Extend the list with the tokens
    return processed


def check_frequency(tokens):
    lyrics_count = {}  # This dictionary will hold a word and the number of times it appears
    word_frequency = Counter(tokens)
    # Find the 10 most common words
    most_common_words = dict(word_frequency.most_common(20))

    # Print the most common words and their frequencies
    for word, num in most_common_words.items():
        lyrics_count[word] = num
        # print(f'{word}: {num}')

    return lyrics_count


def create_bar_graph(count_dict):
    words = list(count_dict.keys())
    appearances = list(count_dict.values())
    plt.figure(figsize=(15, 10))
    plt.bar(range(len(count_dict)), appearances, tick_label=words)
    plt.show()


def create_word_cloud(words):
    # Combine the words into a single string
    text = " ".join([word for word in words.keys()])

    # Generate the word cloud
    word_cloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate_from_frequencies(words)
    plt.figure()
    # This is to make the displayed image appear more smoothly
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def create_bar_chart(word_freq_dict, top_n=10):
    # Sort the word frequency dictionary by values in descending order
    sorted_word_freq = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Extract the top N words and their frequencies
    top_words = [item[0] for item in sorted_word_freq[:top_n]]
    top_freqs = [item[1] for item in sorted_word_freq[:top_n]]

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(top_words, top_freqs)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top {} Words'.format(top_n))
    plt.xticks(rotation=45)
    plt.show()


lyrics_list = get_album_lyrics()
clean_lyrics = process_lyrics(lyrics_list)

word_count = check_frequency(clean_lyrics)
create_word_cloud(word_count)
