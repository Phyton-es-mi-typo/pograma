import abc
import aemet
from app import config


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
    def _get_data(self, request_details, api_key: str):
        raise NotImplementedError

    def retrieve(self, **kwargs):
        data = self._get_data(
            self._get_request_details(**kwargs), self.api_key
        )
        breakpoint()
        return data


class AEMETweatherPredictionByLocation(WeatherProvider):
    def __init__(self, location: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.location = location

    def _get_request_details(self, **kwargs):
        breakpoint()

        municipality = aemet.Municipio.buscar(self.location)[0]
        location_code = municipality.get_codigo()
        return location_code

    def _get_data(self, request_details, api_key: str):
        aemet_client = aemet.Aemet(self.api_key)
        return aemet_client.get_prediccion(request_details)


# "Dateador"`s`
class WeatherPredictionService:
    def __init__(self, weather_provider: WeatherProvider):
        # Dependency injection: WeatherProvider should be abstract class
        self.weather_provider = weather_provider


if __name__ == "__main__":
    weather_service = WeatherPredictionService(
        weather_provider=AEMETweatherPredictionByLocation(
            api_key=config.WEATHER_SERVICE_API_KEY, location="Madrid"
        )
    )
    weather_data = weather_service.weather_provider.retrieve()
    prediction = weather_data.prediccion
