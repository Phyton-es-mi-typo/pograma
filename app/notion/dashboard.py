from fastapi import APIRouter

router = APIRouter(
    prefix='/dashboard',
    tags=['dashboard'],
    responses={404: {'description': 'Not found'}}
)


@router.get('/')
def hello_dashboard():
    return {'hello': 'dashboard'}
