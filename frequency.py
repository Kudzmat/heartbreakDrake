from clean_data import clean_lyrics
from collections import Counter


def check_frequency():
    word_frequency = {}
    for lyrics in clean_lyrics:
        word_frequency.update(Counter(lyrics))
