import joblib


# Load once when the application starts
model = joblib.load("app/ml/intent_model.pkl")
vectorizer = joblib.load("app/ml/vectorizer.pkl")


def detect_intent(message: str):

    message = message.lower().strip()

    # ==========================================
    # Rule-Based High Priority Intents
    # ==========================================

    hr_dashboard_phrases = [
        "hr dashboard",
        "show hr dashboard",
        "company summary",
        "organization summary",
        "today summary",
        "today's summary",
        "daily summary",
        "daily report",
        "hr summary",
    ]

    if any(phrase in message for phrase in hr_dashboard_phrases):
        return "hr_dashboard"

    # ==========================================
    # Machine Learning
    # ==========================================

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)

    return prediction[0]