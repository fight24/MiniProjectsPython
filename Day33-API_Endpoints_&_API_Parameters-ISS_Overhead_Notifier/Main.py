import requests

params = {
    "lat": 36.7201600,
    "lng": -4.4203400,
    "formatted": 0

}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
print(data)
