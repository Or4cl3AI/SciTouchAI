import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def processNaturalLanguage(userInput):
    stop_words = set(stopwords.words('english'))

    tokenized = sent_tokenize(userInput)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)

    return tagged