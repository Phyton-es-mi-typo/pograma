import os
import abc


class WeatherConditions:
    def __init__(
        self, temperature: float, pressure: float, precipitation: float
    ) -> None:
        self.temperature = temperature
        self.pressure = pressure
        self.precipitation = precipitation


class WeatherProvider(metaclass=abc.ABCMeta):
    def __init__(self, api_key):
        self.api_key = api_key

    @abc.abstractmethod
    def _get_request_details(self, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_data(self, request_details, api_key):
        raise NotImplementedError

    def retrieve(self, **kwargs):
        data = self._get_data(
            self._get_request_details(**kwargs), self.api_key
        )
        return data


class AEMETweatherProvider(WeatherProvider):
    def _get_request_details(self):
        pass

    def _get_data(self):
        pass


# "Dateador"
class WeatherService:
    def __init__(self, weather_provider: WeatherProvider):
        # Dependency injection: WeatherProvider should be anabstract class
        self.weather_provider = weather_provider


if __name__ == "__main__":
    weather_service = WeatherService(
        weather_provider=WeatherProvider(os.environ["WEATHER_SERVICE_API_KEY"])
    )
