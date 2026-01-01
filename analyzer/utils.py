import joblib
import os

# Load model and vectorizer
model_path = os.path.join(os.path.dirname(__file__), 'sentiment_model.joblib')
vectorizer_path = os.path.join(os.path.dirname(__file__), 'count_vectorizer.joblib')

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except FileNotFoundError as e:
    print(f"Error loading model files: {e}")
    model = None
    vectorizer = None

def predict_sentiment(text):
    if model is None or vectorizer is None:
        return "Error: Model not loaded"
    
    try:
        X = vectorizer.transform([text])
        prediction = model.predict(X)
        # Convert prediction to string for display
        return str(prediction[0])
    except Exception as e:
        return f"Error: {str(e)}"
