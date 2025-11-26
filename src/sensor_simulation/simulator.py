import time
import random
import requests

API = "http://127.0.0.1:8000/predict/"

print("Simulador iniciado...\n")

while True:
    v = round(random.uniform(0, 1), 2)
    res = requests.post(API, json={"value": v})
    print("Valor enviado:", v, "| Predição:", res.json())
    time.sleep(2)
