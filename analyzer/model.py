import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "sentiment_model.joblib"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "count_vectorizer.joblib"))

def predict_sentiment(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    return prediction
