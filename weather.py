import requests

city = 'Chicago'
url = 'http://api.weatherapi.com/v1/current.json?key=1704749494fc40139c920140252705&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, 'is', description, 'and', temp, 'degrees')