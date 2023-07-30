import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Shared variables
data_set = None
user_input = None

def process_input(user_input):
    """
    Function to process user input using natural language processing techniques
    """
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(user_input)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
    return tagged

def analyze_data(data_set):
    """
    Function to analyze data using natural language processing techniques
    """
    stop_words = set(stopwords.words('english'))
    tokenized = sent_tokenize(data_set)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
    return tagged

def render_visualization(tagged_data):
    """
    Function to render visualization of analyzed data
    """
    entities = nltk.chunk.ne_chunk(tagged_data)
    entities.draw()