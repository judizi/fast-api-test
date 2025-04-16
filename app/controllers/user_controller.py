from http import HTTPStatus

from constants.response_code import ResponseCode
from dto.user_dto import UserCreate
from fastapi.responses import JSONResponse
from service.user_service import (get_user_data_by_id, get_user_data_list,
                                  insert_user_data)
from sqlalchemy.orm import Session
from utils.response import create_response


def get_users(skip: int, limit: int, db: Session) -> JSONResponse:
    response = get_user_data_list(skip, limit, db)
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    if response.code == ResponseCode.SUCCESS:
        http_code = HTTPStatus.OK

    return create_response(
        http_code,
        response
    )
 
def get_user(user_id: str, db: Session) -> JSONResponse:
    response = get_user_data_by_id(user_id, db)
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    if response.code == ResponseCode.SUCCESS:
        http_code = HTTPStatus.OK
    elif response.code == ResponseCode.NOT_FOUND:
        http_code = HTTPStatus.NOT_FOUND

    return create_response(
        http_code,
        response
    )

def insert_user(user: UserCreate, db: Session) -> JSONResponse:
    response = insert_user_data(user, db)
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    if response.code == ResponseCode.CREATED:
        http_code = HTTPStatus.CREATED
    elif response.code == ResponseCode.DUPLICATE_RESOURCE:
        http_code = HTTPStatus.CONFLICT

    return create_response(
        http_code,
        response
    )
