from fastapi import FastAPI

from .notion.dashboard import router as notion
from .weather.weather import router as weather

app = FastAPI()
app.include_router(notion)
app.include_router(weather)


@app.get('/')
def hello_world():
    return {'hello': 'world'}
