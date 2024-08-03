import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

def train_model():
    texts = [
        'I love programming', 'I hate bugs', 'This is awesome', 'This is terrible',
        'Python is great', 'I dislike debugging', 'Machine learning is fascinating',
        'Errors are annoying', 'Coding is fun', 'Debugging is frustrating',
        'I enjoy solving complex problems', 'Simple code is often the best',
        'Programming can be challenging', 'Machine learning models require tuning'
    ]
    labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]
    
    if len(texts) != len(labels):
        raise ValueError("Number of texts and labels must be the same")
    
    global pipeline
    pipeline = make_pipeline(CountVectorizer(), MultinomialNB())
    pipeline.fit(texts, labels)

def process_input(text):
    # Use the pipeline to make predictions
    prediction = pipeline.predict([text])
    return 'Positive' if prediction[0] == 1 else 'Negative'

# Train the model when the module is loaded
train_model()
