from fastapi import APIRouter

router = APIRouter(
    prefix='/weather',
    tags=['weather'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
def hello_weather():
    return {'hello': 'weather'}
