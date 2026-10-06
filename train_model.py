import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv("data/processed_data.csv")

features = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "MA5",
    "MA20",
    "Return",
    "Volatility"
]

X = data[features]
y = data["Target"]

split = int(len(data) * 0.8)

X_train = X.iloc[:split]
X_test = X.iloc[split:]

y_train = y.iloc[:split]
y_test = y.iloc[split:]

print("Training data:", len(X_train))
print("Testing data:", len(X_test))

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

joblib.dump(model, "model/stock_model.pkl")

print("\nModel saved successfully.")