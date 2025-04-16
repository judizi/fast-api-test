from http import HTTPStatus

from config.settings import settings
from constants.response_code import ResponseCode
from constants.response_messages import RESPONSE_MESSAGES
from fastapi.responses import JSONResponse
from utils.response import create_response, create_response_dto


def get_api() -> JSONResponse:
    return create_response(
        HTTPStatus.OK,
        create_response_dto(
            code=ResponseCode.SUCCESS, 
            message=RESPONSE_MESSAGES.get(ResponseCode.SUCCESS), 
            data={"appName": settings.app_name, "appVersion": settings.app_version})
    )
