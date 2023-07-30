```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Shared variable
user_input = ""

def processInput():
    global user_input

    # Tokenization of text
    tokens = sent_tokenize(user_input)
    for i in tokens:
        words = nltk.word_tokenize(i)

        # Removing stop words
        new_words = [word for word in words if word.isalnum()]

        # Using a Tagger. Which is part-of-speech tagger or POS-tagger. 
        tagged = nltk.pos_tag(new_words)

        # Named entity recognition
        namedEnt = nltk.ne_chunk(tagged)
        namedEnt.draw()

if __name__ == "__main__":
    user_input = input("Enter text to process: ")
    processInput()
```