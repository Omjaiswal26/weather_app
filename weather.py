import requests

def get_weather(city):
    api_key = "APIKEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            country = data["sys"]["country"]

            print(f"Weather in {city.title()}, {country}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("City not found. Please enter a valid city name.")
    except Exception as e:
        print("An error occurred:", e)

while True:
    city = input("Enter the city name: ")
    get_weather(city)
    cont = input("Do you want to search another city?")
    if cont == 'Yes' or cont=='yes':
        continue
    else:
        break
