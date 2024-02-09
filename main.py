import requests
from twilio.rest import Client
account_sid = "AC85929387276a310d7b4564179d3b8994"
auth_token = "585a1be86942f8c2fe2ff047c65902bb"
api_key = "a7f668906006dffaa9e26b8d30d6c2de"
# MY_LAT = 30.348000
MY_LAT = -6.175110
# MY_LONG = 78.393303
MY_LONG = 106.865036
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂",
        from_="+16592465627",
        to="+918091766903"
    )
    print(message.status)
