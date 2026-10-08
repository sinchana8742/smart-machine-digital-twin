from flask import Flask, render_template, jsonify, request
import random
import os
import pickle
from datetime import datetime

app = Flask(__name__)

MODEL_PATH = "model.pkl"

def train_fallback_model():
    """Train a small Random Forest model if model.pkl does not exist."""
    from sklearn.ensemble import RandomForestClassifier

    X, y = [], []
    random.seed(42)

    # Synthetic operating states
    for _ in range(500):
        state = random.choice(["NORMAL", "WARNING", "CRITICAL"])

        if state == "NORMAL":
            temp = random.uniform(45, 72)
            vibration = random.uniform(0.5, 3.0)
            rpm = random.uniform(1350, 1550)
            power = random.uniform(3.0, 5.5)
        elif state == "WARNING":
            temp = random.uniform(70, 88)
            vibration = random.uniform(2.5, 5.5)
            rpm = random.uniform(1200, 1450)
            power = random.uniform(5.0, 7.5)
        else:
            temp = random.uniform(85, 105)
            vibration = random.uniform(5.0, 9.0)
            rpm = random.uniform(900, 1300)
            power = random.uniform(7.0, 10.5)

        X.append([temp, vibration, rpm, power])
        y.append(state)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    return model

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
else:
    model = train_fallback_model()

def generate_sensor_data(mode="normal"):
    if mode == "overheating":
        return {
            "temperature": round(random.uniform(88, 102), 1),
            "vibration": round(random.uniform(2.5, 5.0), 1),
            "rpm": round(random.uniform(1100, 1350), 0),
            "power": round(random.uniform(6.5, 9.0), 1),
        }
    if mode == "vibration":
        return {
            "temperature": round(random.uniform(65, 80), 1),
            "vibration": round(random.uniform(6.0, 9.0), 1),
            "rpm": round(random.uniform(1150, 1400), 0),
            "power": round(random.uniform(5.5, 8.0), 1),
        }
    if mode == "power":
        return {
            "temperature": round(random.uniform(70, 85), 1),
            "vibration": round(random.uniform(2.5, 5.0), 1),
            "rpm": round(random.uniform(1150, 1400), 0),
            "power": round(random.uniform(8.0, 10.5), 1),
        }

    return {
        "temperature": round(random.uniform(50, 72), 1),
        "vibration": round(random.uniform(0.7, 2.8), 1),
        "rpm": round(random.uniform(1380, 1520), 0),
        "power": round(random.uniform(3.2, 5.4), 1),
    }

def predict(data):
    values = [[data["temperature"], data["vibration"], data["rpm"], data["power"]]]
    status = model.predict(values)[0]

    # A simple transparent rule layer makes the prototype easier to explain.
    if data["temperature"] >= 90 or data["vibration"] >= 7 or data["power"] >= 9.5:
        status = "CRITICAL"
    elif data["temperature"] >= 75 or data["vibration"] >= 4.5 or data["power"] >= 7.0:
        status = "WARNING"

    health = 100
    health -= max(0, data["temperature"] - 60) * 0.45
    health -= max(0, data["vibration"] - 2) * 4
    health -= max(0, data["power"] - 5) * 3
    health += max(0, data["rpm"] - 1350) * 0.015
    health = max(0, min(100, health))

    if status == "NORMAL":
        recommendation = "Machine operating normally. Continue routine monitoring."
    elif status == "WARNING":
        recommendation = "Inspect machine conditions and schedule preventive maintenance."
    else:
        recommendation = "High-risk condition detected. Inspect machine immediately."

    return status, round(health), recommendation

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/sensor")
def sensor():
    mode = request.args.get("mode", "normal")
    data = generate_sensor_data(mode)
    status, health, recommendation = predict(data)

    return jsonify({
        **data,
        "status": status,
        "health": health,
        "recommendation": recommendation,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })

if __name__ == "__main__":
    app.run(debug=True)
