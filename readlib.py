import math
import re
import requests

from nltk.corpus import cmudict
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize

from bs4 import BeautifulSoup

d = cmudict.dict()
tokenizer = RegexpTokenizer(r'\w+')


class Readability:

    def __init__(self, url):
        self.url = url

    def get_url(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text)
        return soup.get_text()

    def sent_tokenize(self):
        return sent_tokenize(self.get_url())

    def word_tokenize(self):
        return tokenizer.tokenize(self.get_url())

    def char(self):
        char = 0
        for word in self.word_tokenize():
            for w in word:
                char += 1

        return char

    def sent_count(self):
        return len(self.sent_tokenize())

    def word_count(self):
        return len(self.word_tokenize())

    def syl(self, word):
        # returns number of syllables per word
        try:
            syllable = [len(list(y for y in x if y[-1].isdigit()))
                        for x in d[word.lower()]]
            return syllable[0]

        except KeyError:
            return None

    def list_to_word(self):
        # tokenizes all words. For each token, the syl function is called.
        # Returns the number of syllables for each token in a list.
        len_syl = []
        word = self.word_tokenize()

        for w in word:
            len_syl.append(self.syl(w))

        return len_syl

    def avg_syl(self):
        return sum(self.list_to_word()) / self.word_count()

    def avg_char(self):
        return self.char() / self.word_count()

    def avg_words(self):
        return self.word_count() / self.sent_count()

    def poly_syl(self):
        poly_syl = []

        for p in self.list_to_word():
            if p >= 3:
                poly_syl.append(p)

        return poly_syl

    def flesch_kincaid(self, ease=False):
        # Flesch Kincaid algorithm determines the readability ease of a given text.
        # Higher score indicates easier comprehension and lower score indicates more complexity
        syl_int = sum(self.list_to_word())
        TWS = self.word_count() / self.sent_count()
        TSW = syl_int / self.word_count()

        if ease:
            return 206.835 - 1.015 * TWS - 84.6 * TSW

        else:
            x = 0.39 * TWS + 11.8 * TSW - 15.59
            return "Flesch-Kincaid Grade Level: {}".format(x)

    def gunning_fog(self):
        counter = len(self.poly_syl())
        TWS = self.word_count() / self.sent_count()
        CWW = counter / self.word_count()
        fog = 0.4 * (TWS + 100 * CWW)
        return "Gunning Fog Index: {}".format(fog)

    def smog_index(self):
        # for accuracy, there must be at least 30 sentences
        f = len(self.poly_syl()) * (30 / self.word_count())
        smog = 1.0430 * math.sqrt(f) + 3.1291
        return "Smog Index: {}".format(smog)

    def ari(self):
        chars = self.char()
        f = 4.71 * (chars / self.word_count()) + 0.5 * (self.word_count() / self.sent_count()) - 21.43
        return "Automated Readability Index: {}".format(f)





