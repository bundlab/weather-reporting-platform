import requests
from .config import OPENWEATHER_API_KEY

def get_weather(city: str):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )
    res = requests.get(url).json()

    return {
        "city": city,
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "description": res["weather"][0]["description"],
    }
