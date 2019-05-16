# Write a function that returns the most common (non stop)word in this Harry Potter text.

# Make sure you strip out non-alphanumeric characters and stopwords. Your function should return a tuple of (most_common_word, frequency) (former lowercased).

# The template code already loads the Harry Potter text and list of stopwords in.

# Check the tests for more info - have fun!


import os
import urllib.request
import string

from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with open(stopwords_file) as stopwords:
    	stop = stopwords.read()

    with open(harry_text) as hp:
    	hp_words = hp.read()
    	hp_ascii = hp_words.translate(str.maketrans('', '', (string.punctuation + string.digits)))

    word_list = [word.lower() for word in hp_ascii.split()if word.lower() not in stop]

    return Counter(word_list).most_common(1)[0]