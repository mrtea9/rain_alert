import requests
from twilio.rest import Client


MY_LAT = 47.0056
MY_LONG = 28.8575
api_key = ""
OWM_url = "http://api.openweathermap.org/data/2.5/forecast"
account_sid = ""
auth_token = ""


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}


response = requests.get(OWM_url, params=parameters)
response.raise_for_status()
data = response.json()
list_data = data["list"]

will_rain = False
for hour_data in list_data:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="O sa fie ploaie, vezi cum te imbraci",
        from_="+12058093489",
        to="",
    )

    print(message.status)
