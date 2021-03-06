import nltk
import unidecode
import string
import os
import re
from nltk.corpus import stopwords
#necessario para os calculos de frequencia


stop_words = stopwords.words('portuguese')

class Preprocessing:
    def __init__(self):
        self.sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')
        self.stemmer = nltk.stem.RSLPStemmer()
    # remover acentos
    def remove_accents(self, text):
        texto = unidecode.unidecode(text)
        return texto
    # remover pontuacoes
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('','',string.punctuation))
    #dividir o texto em sentencas
    def tokenize_sentences(self, text):
        sentences = self.sent_tokenizer.tokenize(text)
        return sentences
    # tokenizar o texto
    def tokenize_words(self, text):
        tokens = nltk.tokenize.word_tokenize(text)
        return tokens
    #stemizar
    def stemmize(self, tokens):
        return [self.stemmer.stem(word) for word in tokens]
    #colocar as palavras em letras minusculas
    def lowercase(self, text):
        return text.lower()
    #remover stopwords com base na lista de stopwords do nltk
    def removeUrl(self, text):
        text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
        return(text)
    def removeContraBarraN(self, text):
        text = text.replace('\n', '')
        return text
