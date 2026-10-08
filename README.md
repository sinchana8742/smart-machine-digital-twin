# Smart Machine Digital Twin

A small interview-ready Digital Twin prototype for **predictive maintenance**.

## Concept

The application represents an industrial machine using a virtual model. Python simulates sensor readings for:

- Temperature
- Vibration
- RPM
- Power consumption

A Random Forest model classifies the machine condition as:

- NORMAL
- WARNING
- CRITICAL

The Flask dashboard displays the current virtual machine state and lets you simulate faults.

## Architecture

Physical Machine (conceptual)
→ IoT/Sensor Data
→ Digital Twin
→ ML Analytics
→ Prediction
→ Maintenance Recommendation

In this prototype, the sensor layer is simulated in Python. In a real system, the simulator can be replaced by actual IoT sensors and a communication layer such as MQTT.

## Run the project

### 1. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Optional: generate the training dataset

```bash
python generate_data.py
```

### 4. Optional: train the model

```bash
python train_model.py
```

This creates `model.pkl`.

### 5. Start the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Interview explanation

This is a **prototype Digital Twin**, not a complete industrial deployment.

A strong explanation is:

> "I built a Python and Flask-based Digital Twin prototype for an industrial machine. Since I did not have physical hardware, I simulated sensor data for temperature, vibration, RPM and power. The virtual machine state is updated from these readings, and a machine-learning model predicts whether the machine is normal, in warning condition or critical. In a real deployment, the simulated data source could be replaced with IoT sensors and a real-time communication layer."

## Possible future improvements

- Connect ESP32/Raspberry Pi sensors
- MQTT for real-time communication
- Store historical data in a time-series database
- Add anomaly detection
- Add predictive failure probability
- Add physics-based machine model
- Add authentication and role-based access
- Deploy on a cloud platform
