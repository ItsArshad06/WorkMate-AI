import joblib


# Load once when the application starts
model = joblib.load("app/ml/intent_model.pkl")
vectorizer = joblib.load("app/ml/vectorizer.pkl")


def detect_intent(message: str):

    message = message.lower()

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)

    return prediction[0]