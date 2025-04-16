from controllers.api_controller import get_api
from dto.api_dto import ApiResponse, get_api_responses
from dto.response_dto import ResponseModel
from fastapi import APIRouter

router = APIRouter()

@router.get(
    path="/", 
    response_model=ResponseModel[ApiResponse],
    responses=get_api_responses
)
def root():
    return get_api()
