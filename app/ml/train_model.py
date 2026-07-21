import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


# ----------------------------------
# Load Dataset
# ----------------------------------

data = pd.read_csv("app/ml/dataset.csv")

X = data["text"]
y = data["intent"]


# ----------------------------------
# Convert Text -> Numbers
# ----------------------------------

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)


# ----------------------------------
# Split Dataset
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)


# ----------------------------------
# Train Model
# ----------------------------------

model = LogisticRegression()

model.fit(X_train, y_train)


# ----------------------------------
# Evaluate
# ----------------------------------

predictions = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, predictions))

print("\nClassification Report:\n")

print(classification_report(y_test, predictions))


# ----------------------------------
# Save Model
# ----------------------------------

joblib.dump(model, "app/ml/intent_model.pkl")
joblib.dump(vectorizer, "app/ml/vectorizer.pkl")

print("\n✅ Model trained successfully!")

print("Saved:")
print("- intent_model.pkl")
print("- vectorizer.pkl")