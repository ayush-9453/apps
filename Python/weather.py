import requests
import json
api = '893274fd421e4b6063d0d07a94c38274'
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city= input("Enter a city name: ")
complete_url = f"{base_url}appid={api}&q={city}"

response = requests.get(complete_url)


if response.status_code == 200: 
    data = response.json()
    weather = data["weather"]
    main = data["main"]
    wind = data["wind"]
    print(f"The weather forecast of {city} is : {weather[0]['main']} ")
    print(f"Wind speed :{wind['speed']}")
    print(f"Temperature : {main['temp']} but feels like: {main['feels_like']}")
else : 
    print('An error occured.')
