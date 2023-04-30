import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
LATITUDE = 54.35
LONGITUDE = 18.65
API_KEY = "appid"

ACCOUNT_SID = "account_sid"
AUTH_TOKEN = "auth_token"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]

weather_conditions = {
    "2": "Thunderstorm 🌩️",
    "3": "Drizzle 🌧️",
    "5": "Rain ☂️",
    "6": "Snow ⛄",
    "7": "Fog 😶‍🌫️",
    "8": "Clouds ⛅",
    "800": "Clear sky ☀️"
}

client = Client(ACCOUNT_SID, AUTH_TOKEN)

if int(condition_code) == 800:
    message = client.messages.create(
        body=f"{weather_conditions['800']}",
        from_="+16205268968",
        to="+48*********"
    )
    print(message.status)
elif str(condition_code)[0] in weather_conditions:
    message = client.messages.create(
        body=f"{weather_conditions[str(condition_code)[0]]}",
        from_="+16205268968",
        to="+48*********"
    )
    print(message.status)
