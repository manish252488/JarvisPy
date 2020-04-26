from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "i like it"
analys = TextBlob(text)
print(analys.sentiment)
stops = stopwords.words("english")
lists = word_tokenize(text)
text = ""
for w in lists:
    if w not in stops:
        text = text + " " + str(w)


analysis = TextBlob(text)
print(analysis.sentiment)