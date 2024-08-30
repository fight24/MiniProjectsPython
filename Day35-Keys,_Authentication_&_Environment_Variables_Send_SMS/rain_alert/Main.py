import requests
from twilio.rest import Client
API_KEY = "[your_api]"
account_sid = "[your_acc]"
auth_token = "[your_token]"
LAT = 20.865139
LNG = 106.683830
weather_params = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY,
    "cnt": 4
}
will_rain = False

client = Client(username=account_sid, password=auth_token)

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()
list_weather_data = [i["weather"] for i in weather_data["list"]]
dict_id_and_time = {
    "id": [],
    "time": [i["dt_txt"] for i in weather_data["list"]],
    "will_rain": []
}
for i in range(len(list_weather_data)):
    # print(list_weather_data[i])
    conditions_code = list_weather_data[i][0]["id"]
    dict_id_and_time["id"].append(conditions_code)
    if conditions_code < 700:
        dict_id_and_time["will_rain"].append(True)
        will_rain = True
    else:
        dict_id_and_time["will_rain"].append(False)
# print("Bring an Umbrella")
date_time = [dict_id_and_time["time"][x] for x in range(len(dict_id_and_time["time"])) if dict_id_and_time["will_rain"][x]]
message = None
if will_rain:
    message = client.messages.create(
        to="+8",
        from_='[phone number]',
        body=f"it's going to rain on {' , '.join(date_time)}. Remember to bring an ☂"


    )
print(message.status)
print(dict_id_and_time)
# print(type(weather_data["list"]))
# print(response.status_code)
# print(response.json())
