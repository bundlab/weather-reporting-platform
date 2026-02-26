import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY")
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://weather:weather@db:5432/weather_db"
)
