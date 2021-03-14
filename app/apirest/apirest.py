from fastapi import FastAPI

from .notion.routes import router as notion
from .weather.routes import router as weather

app = FastAPI(title='Tyempo')
app.include_router(notion)
app.include_router(weather)


@app.get('/')
def hello_world():
    return {'hello': 'world'}
