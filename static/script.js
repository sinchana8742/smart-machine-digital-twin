async function loadData(mode = "normal") {
    const response = await fetch(`/api/sensor?mode=${mode}`);
    const data = await response.json();

    document.getElementById("temperature").textContent = data.temperature;
    document.getElementById("vibration").textContent = data.vibration;
    document.getElementById("rpm").textContent = data.rpm;
    document.getElementById("power").textContent = data.power;
    document.getElementById("health").textContent = data.health + "%";
    document.getElementById("prediction").textContent = data.status;
    document.getElementById("recommendation").textContent = data.recommendation;
    document.getElementById("timestamp").textContent = data.timestamp;

    const status = document.getElementById("status");
    status.textContent = data.status;
    status.className = "status " + data.status.toLowerCase();

    const ring = document.querySelector(".health-ring");
    ring.style.borderWidth = "12px";
    if (data.health < 40) {
        ring.style.borderStyle = "dashed";
    } else {
        ring.style.borderStyle = "solid";
    }
}

loadData("normal");
setInterval(() => loadData("normal"), 10000);
