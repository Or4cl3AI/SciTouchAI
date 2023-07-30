```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Shared variable
dataSet = None
userInput = None

def process_user_input(userInput):
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(userInput)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
    return tagged

def analyze_data(dataSet):
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(dataSet)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
    return tagged

def natural_language_processing(userInput, dataSet):
    user_input_processed = process_user_input(userInput)
    data_processed = analyze_data(dataSet)
    return user_input_processed, data_processed
```