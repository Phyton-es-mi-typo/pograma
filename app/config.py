import os
from dotenv import load_dotenv
from pathlib import Path

dotfile = Path(__file__).resolve().parents[1] / ".env"

load_dotenv(dotfile)

WEATHER_SERVICE_API_KEY = os.environ["WEATHER_SERVICE_API_KEY"]
