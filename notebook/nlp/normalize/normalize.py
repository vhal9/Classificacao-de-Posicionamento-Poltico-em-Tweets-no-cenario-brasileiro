import pandas as pd
import numpy as np
import re
import os
import spacy
from nlp import lexical

class Normalize:
    def __init__(self):
        self.normalizer = lexical.Preprocessing()
    
    #as quatro funcoes abaixo retiram lixos encontrados nos textos
    def remove_username(self, tweet):
        return re.sub('@[^\s]+','',tweet)
    def remove_url(self, text):
        text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
        return(text)
    def remove_end_of_line(self, tweet):
        return tweet.replace('\n', '').replace('RT', '')
    def remove_duplicate_letters(self, tweet):
        # ([^rs])  - Qualquer letra que não r ou s
        # (?=\1+)  - Que se repita uma vez ou mais
        # |(rr)    - Ou dois r's
        # (?=r+)   - Que tenham mais r's à frente
        # |(ss)    - Ou dois s's
        # (?=s+)   - Que tenham mais s's à frente
        regex = r"([^rs])(?=\1+)|(rr)(?=r+)|(ss)(?=s+)"
        tweet = re.sub(regex, '', tweet, 0)
        return tweet
    def normalize(self, tweet):
        tweet = self.normalizer.lowercase(tweet)
        tweet = self.normalizer.remove_accents(tweet)
        tweet = self.remove_username(tweet)
        tweet = self.remove_end_of_line(tweet)
        tweet = self.remove_url(tweet)
        tweet = self.remove_duplicate_letters(tweet)
        tweet = self.normalizer.remove_punctuation(tweet)
        #tweet = self.normalizer.tokenize_words(tweet)
        return tweet