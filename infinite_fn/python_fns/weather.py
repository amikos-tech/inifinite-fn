import random


def fetch_weather_data(location: str, date: str = None) -> dict:
    """
    Fetch weather data for the specified location and date.

    This function currently returns random dummy data. In a real-world implementation,
    it would make a request to a weather data API and return the result.

    :param location: The location to fetch weather data for.
    :param date: The date to fetch weather data for. If not specified, fetches current
                 weather data. Dates should be specified in YYYY-MM-DD format.
    :return: A dictionary containing weather data.
    """

    # Dummy weather data
    weather_data = {
        'location': location,
        'date': date if date else 'current',
        'temperature': random.randint(-30, 50),  # Temperature in degrees Celsius
        'humidity': random.randint(0, 100),  # Humidity in percentage
        'rainfall': random.randint(0, 50) if random.random() < 0.3 else 0,  # 30% chance of rain
        'wind_speed': random.randint(0, 20),  # Wind speed in km/h
        'wind_direction': random.choice(['N', 'S', 'E', 'W']),  # Wind direction
        'pressure': random.randint(950, 1050),  # Atmospheric pressure in hPa
        'UV_index': random.randint(0, 11)  # UV index
    }

    return weather_data


def current_weather(location: str) -> dict:
    """
    Fetch current weather data for the specified location.

    :param location: The location to fetch current weather data for.
    :return: A dictionary containing current weather data.
    """
    return fetch_weather_data(location)


def forecast_weather(location: str, days: int) -> list:
    """
    Fetch weather forecast data for the specified location for a number of days.

    :param location: The location to fetch forecast weather data for.
    :param days: The number of days to fetch the forecast for.
    :return: A list of dictionaries each containing weather data for a day.
    """
    forecast = [fetch_weather_data(location) for _ in range(days)]
    return forecast


def historical_weather(location: str, date: str) -> dict:
    """
    Fetch historical weather data for the specified location and date.

    :param location: The location to fetch historical weather data for.
    :param date: The date to fetch historical weather data for. Dates should be specified in YYYY-MM-DD format.
    :return: A dictionary containing historical weather data.
    """
    return fetch_weather_data(location, date)


def average_temperature(location: str, days: int = 30) -> float:
    """
    Calculate the average temperature for the specified location over a number of past days.

    :param location: The location to calculate the average temperature for.
    :param days: The number of past days to calculate the average over. Default is 30.
    :return: The average temperature over the specified number of days.
    """
    # Fetch historical weather data for the specified number of days
    historical_data = forecast_weather(location, days)

    # Calculate the average temperature
    total_temperature = sum(day['temperature'] for day in historical_data)
    average_temp = total_temperature / days

    return average_temp


def max_min_temperature(location: str, days: int = 30) -> tuple:
    """
    Calculate the maximum and minimum temperature for the specified location over a number of past days.

    :param location: The location to calculate the maximum and minimum temperature for.
    :param days: The number of past days to calculate the maximum and minimum over. Default is 30.
    :return: A tuple where the first element is the maximum temperature and the second element is the minimum temperature over the specified number of days.
    """
    # Fetch historical weather data for the specified number of days
    historical_data = forecast_weather(location, days)

    # Calculate the maximum and minimum temperature
    max_temperature = max(day['temperature'] for day in historical_data)
    min_temperature = min(day['temperature'] for day in historical_data)

    return (max_temperature, min_temperature)


def rain_chance(location: str, hours: int = 24) -> float:
    """
    Calculate the chance of rain for the specified location over the next number of hours.

    :param location: The location to calculate the rain chance for.
    :param hours: The number of hours to calculate the rain chance over. Default is 24.
    :return: The chance of rain over the specified number of hours as a percentage.
    """
    # Fetch forecast data for the specified number of hours
    # For simplicity, we're using daily forecast data here, so we divide hours by 24
    days = hours // 24
    forecast_data = [fetch_weather_data(location) for _ in range(days)]

    # Calculate the chance of rain
    # For simplicity, we're assuming that if rainfall is > 0, it's raining
    rainy_days = sum(1 for day in forecast_data if day['rainfall'] > 0)
    return (rainy_days / days) * 100 if days > 0 else 0


def uv_index(location: str) -> int:
    """
    Fetch the UV index for the specified location.

    :param location: The location to fetch the UV index for.
    :return: The UV index for the specified location.
    """
    # For this demonstration, we are using the 'fetch_weather_data' function to get dummy data
    # In a real-world application, we would fetch the UV index data from an appropriate source

    weather_data = fetch_weather_data(location)
    return weather_data['UV_index']


def humidity(location: str) -> int:
    """
    Fetch the current humidity for the specified location.

    :param location: The location to fetch the humidity for.
    :return: The current humidity for the specified location.
    """
    # Fetch weather data for the specified location
    weather_data = fetch_weather_data(location)
    return weather_data['humidity']


def wind_speed(location: str) -> float:
    """
    Fetch the current wind speed for the specified location.

    :param location: The location to fetch the wind speed for.
    :return: The current wind speed for the specified location.
    """
    # Fetch weather data for the specified location
    weather_data = fetch_weather_data(location)
    return weather_data['wind_speed']


def feels_like_temperature(location: str) -> float:
    """
    Calculate the "feels like" temperature for the specified location.

    :param location: The location to calculate the "feels like" temperature for.
    :return: The "feels like" temperature for the specified location.
    """
    # Fetch weather data for the specified location
    weather_data = fetch_weather_data(location)

    # Simple formula to calculate "feels like" temperature
    # This is a dummy formula and does not reflect actual methods of calculating "feels like" temperature
    feels_like_temp = weather_data['temperature'] + (0.05 * weather_data['humidity']) - (
            0.04 * weather_data['wind_speed'])

    return feels_like_temp
