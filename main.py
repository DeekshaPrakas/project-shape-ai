import requests
#import os
from datetime  import datetime
api_key='d01573e1ae24bd1e11da4324c3c05960'
location= input("enter the name of the city: ")
complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()

temp_city=((api_data['main']['temp'])- 273.15)
weather_desc=api_data['weather'][0]['description']
humidity=api_data['main']['humidity']
wind_speed=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %y | %I:%M:%S %p")
print("-----------------------------------------")
print("weather stats for -{} || {}".format(location.upper(),date_time))
print("----------------------------------------------")
print("current temperature is:{: .2f} deg C".format(temp_city))
print("current weather desc :", weather_desc)
print("current humidity :",humidity, '%')
print("current wind speed :", wind_speed,'kmph')