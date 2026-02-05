from fastapi import APIRouter
import math
import requests
from fastapi.responses import Response
import dotenv
import os

ApiRouter = APIRouter(
    prefix="/api",
    tags=["API interna"]
)

# Carregar .env
dotenv.load_dotenv()
apiKey = os.getenv("OPENWEATHER_TOKEN")
# Pegar informações do clima de acordo com a cidade
@ApiRouter.get("/getweather")
def getWeather(city: str = ""):
    # Request de dados da cidade usando OpenWeatherAPI
    req1 = requests.request("get", "http://api.openweathermap.org/geo/1.0/direct?q={0}&limit=1&appid={1}".format(city, apiKey))
    if not req1.json():
        return Response(status_code=404)
    cityInfo = req1.json()[0]
    if str(cityInfo['name']).lower() != city.lower():
        return Response(status_code=404)
    # Request do clima
    req2 = requests.request("get", "https://api.openweathermap.org/data/3.0/onecall?lat={0}&lon={1}&appid={2}&units=metric&exclude=minutely,hourly,alerts".format(cityInfo["lat"], cityInfo["lon"], apiKey))
    weatherData = req2.json()

    weather = weatherData["current"]["weather"]

    # Tratamento dos dados
    wind = float(weatherData["current"]["wind_speed"])
    humidity = math.floor(weatherData["current"]["humidity"])
    temperature = math.floor(weatherData["current"]["temp"])
    temperature_min = math.floor(weatherData["daily"][0]["temp"]["min"])
    temperature_max = math.floor(weatherData["daily"][0]["temp"]["max"])
    icon = str(weather[0]["icon"])

    return {
        "city": city.capitalize(),
        "weather": weather,
        "wind": wind,
        "humidity": humidity,
        "temperature": {
            "current": temperature,
            "min": temperature_min,
            "max": temperature_max
        },
        "icon": icon,
    }