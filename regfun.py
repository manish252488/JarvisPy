from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

punctuator = wordpunct_tokenize(open("localdb/punct.txt", "rt").read())
stopwords = set(stopwords.words("english"))


def remove_pun(sample):
    words = word_tokenize(sample)
    filtered = []
    for w in words:
        if w not in punctuator:
            filtered.append(w)
    return filtered

