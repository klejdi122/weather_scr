import requests

API_KEY = "ecf40b14f518002cd7603f37f521e954"
CITY = "Tirana"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

URL = f"{BASE_URL}q={CITY}&appid={API_KEY}"

def get_weather():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = data['weather'][0]
        
        print(f"Weather in {CITY}:")
        print(f"Temperature: {main_data['temp']}K")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Weather: {weather_data['description']}")
    else:
        print("City not found!")

if __name__ == "__main__":
    get_weather()
