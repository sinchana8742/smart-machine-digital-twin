import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("machine_data.csv")

X = df[["temperature", "vibration", "rpm", "power"]]
y = df["status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred) * 100, 2), "%")
print(classification_report(y_test, pred))

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Saved model.pkl")
