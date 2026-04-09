import requests

URL = "https://totemmflex.onrender.com/interactions/"

for i in range(50):
    response = requests.post(URL, json={
        "sensor_type": "toque",
        "valor": 0.5
    })

    print(f"Enviado {i+1} - Status: {response.status_code}")