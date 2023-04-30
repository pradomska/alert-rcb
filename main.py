import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
LATITUDE = 54.35
LONGITUDE = 18.65
API_KEY = "1633515eea2b90d6d7fe64d16c9367c4"

ACCOUNT_SID = "ACed99dee86823f4e65269e783a7604e42"
AUTH_TOKEN = "80fe9d2fbcbfa696ce3878282775b89f"

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]
if int(condition_code) < 700:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+16205268968",
        to="+48600171513"
    )
    print(message.status)
