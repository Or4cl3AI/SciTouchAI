```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def process_user_input(user_input):
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(user_input)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
    return tagged

def analyze_sentiment(user_input):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(user_input)
    return sentiment

def natural_language_processing(user_input):
    processed_input = process_user_input(user_input)
    sentiment = analyze_sentiment(user_input)
    return processed_input, sentiment
```