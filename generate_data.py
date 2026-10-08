import csv
import random

random.seed(42)

rows = []
for _ in range(1000):
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

    rows.append([round(temp, 2), round(vibration, 2), round(rpm, 0), round(power, 2), state])

with open("machine_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["temperature", "vibration", "rpm", "power", "status"])
    writer.writerows(rows)

print("Created machine_data.csv with", len(rows), "records.")
