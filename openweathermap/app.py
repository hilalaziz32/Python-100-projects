import requests
import smtplib
from q1 import *

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

latitude = 24.911934
longitude =  67.200650


parameters= {
    "lat" : latitude,
    "lon" : longitude,
    "appid" : api_key,
    "cnt" : 3
}

response = requests.get(OWM_Endpoint,parameters)

data = response.json()
print(data)

will_rain = False
for three_hour_data in data["list"]:
    cc = three_hour_data["weather"][0]["id"]
    if cc < 700:
        will_rain = True
        break


if will_rain:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="k224115@nu.edu.pk",
            msg= f"Subject:hey take umbrella\n\nIt is raining please take Umbrella."
        )
else:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="k224115@nu.edu.pk",
            msg= f"Subject:hey no need to worry\n\nIt is not  raining don't take Umbrella."
        )

