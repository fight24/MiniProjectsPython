import time

import requests
from datetime import datetime
import Config
MY_LAT = 21.027763
MY_LONG = 105.834160


def is_iss_overhead():
    res = requests.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    data_iss = res.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = str(datetime.now()).split(" ")[1].split(":")[0]
    print(time_now)
    if int(time_now) >= sunset or int(time_now) < sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send email me to tell me to look up.
# BONUS: run the code every 60 seconds
while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        connect = Config.Config()
        connect.send_mail(
            to_addr="swordartonline242001@gmail.com",
            text="Subject:Look up 👆\n\n The Iss above you in the sky."
            )
        connect.connection_close()



