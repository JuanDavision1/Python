import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = """ He fracasado más de lo que hubiera debido
 
"""

stop_words = set(stopwords.words('spanish'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)