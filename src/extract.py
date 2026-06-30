import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&hourly=temperature_2m")
data = response.json()

def extract():
    "To extract data from the open meteo API"
