import requests

API_KEY = '04d58e741cdcde6f70333d0b1bc4320e'
URL = 'https://api.openweathermap.org/data/2.5/weather'


def weather_data(query):
    params = {'q': {query}, 'appid': {API_KEY}, 'units': 'metric'}
    res = requests.get(URL, params=params)
    return res.json()


def print_weather(result, city):
    print(f"{city}, {result['main']['temp']} degree by Celsius but feels like {result['main']['feels_like']}")


def main():
    city = input("Enter your city: ")
    try:
        weather = weather_data(city)
        print_weather(weather, city)
    except Exception as e:
        print("Oops!", e, "occurred.")


if __name__ == '__main__':
    main()
