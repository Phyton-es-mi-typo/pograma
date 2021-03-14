from app.weather import entities


def test_weather_conditions():
    temperature = 8.3
    pressure = 1002.71
    precipitation = 0.25
    weather_conditions = entities.WeatherConditions(
        temperature=temperature, pressure=pressure, precipitation=precipitation
    )
    assert weather_conditions.temperature == temperature
