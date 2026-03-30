import os
import sys
import httpx

from dotenv import load_dotenv


def get_weather(city_name: str) -> str:
    """Возвращает строку с погодой или сообщением об ошибке."""
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    if not api_key:
        return "Ошибка: не найден OPEN_WEATHER_API_KEY в .env файле"

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
        "lang": "ru"
    }

    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            city_name = data.get("name")
            country = data["sys"].get("country", "")
            temp = round(data["main"]["temp"], 1)
            feels_like = round(data["main"]["feels_like"], 1)
            description = data["weather"][0]["description"].capitalize()

            location = f"{city_name}, {country}" if country else city_name
            return (
                f"Погода в {location}:\n"
                f"Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"{description}"
            )

        elif response.status_code == 404:
            return f"Город '{city}' не найден. Попробуйте добавить страну, например: Moscow,RU"
        elif response.status_code == 401:
            return "Ошибка: неверный API-ключ"
        elif response.status_code == 429:
            return "Ошибка: превышен лимит запросов к API"
        else:
            error_msg = response.json().get("message", response.text)
            return f"Ошибка API ({response.status_code}): {error_msg}"

    except httpx.RequestError as e:
        return f"Ошибка сети при запросе к API: {e}"
    except Exception as e:
        return f"Неожиданная ошибка: {e}"


if __name__ == "__main__":
    load_dotenv()
    if len(sys.argv) < 2:
        print("Использование: python weather.py <Название_города>")
        print("Пример: python weather.py Moscow")
        sys.exit(1)

    city = sys.argv[1]
    result = get_weather(city)
    print(result)
