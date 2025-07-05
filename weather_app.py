import requests

#function to call weather API
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        print(f"\nWeather in {city.title()}: ")
        print(f" Temperature: {main['temp']} C")
        print(f"Humidity: {main['humidity']} %")
        print(f"Condition: {weather['description'].title()}")
    else:
        print("City not found ar API error")


#main App
def main():
    print("=== Weather App ===")

    api_key = input("Enter your OpenWeather API key: ").strip()

    while True:
        city = input("n\Enter city name(or type 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Goodbye!")
            break
        get_weather(city, api_key)

if __name__ == "__main__":
    main()
