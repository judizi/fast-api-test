from http import HTTPStatus

from constants.response_code import ResponseCode
from fastapi.responses import JSONResponse
from service.user_service import get_user_by_id, get_user_list
from sqlalchemy.orm import Session
from utils.response import create_response


def get_users(skip: int, limit: int, db: Session) -> JSONResponse:
    response = get_user_list(skip, limit, db)
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    if response.get("code") == ResponseCode.SUCCESS:
        http_code = HTTPStatus.OK

    return create_response(
        http_code,
        response
    )
 
def get_user(user_id: str, db: Session) -> JSONResponse:
    response = get_user_by_id(user_id, db)
    http_code = HTTPStatus.INTERNAL_SERVER_ERROR
    if response.get("code") == ResponseCode.SUCCESS:
        http_code = HTTPStatus.OK
    elif response.get("code") == ResponseCode.NOT_FOUND:
        http_code = HTTPStatus.NOT_FOUND

    return create_response(
        http_code,
        response
    )
