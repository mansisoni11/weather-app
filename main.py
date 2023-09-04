import requests
import json
import os
city = input("enter name of city")
url = f"https://api.weatherapi.com/v1/current.json?key=86ab859815b0438c9b5122817232008&q={city}"
r= requests.get(url)
print(type(r.text))
wdic=json.loads(r.text)
w = wdic["current"]["temp_c"]
os.system(f"say 'The current weather in {city} is {w} degrees' ")
