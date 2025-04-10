from typing import Optional

from dto.response_dto import ResponseModel
from fastapi.responses import JSONResponse


def create_response(http_code: int, content: dict) -> JSONResponse:
    return JSONResponse(
        status_code=http_code,
        content=content
    )

def create_response_dto(code: int, message: str, data=None) -> dict:
    return ResponseModel(code=code, message=message, data=data).model_dump(exclude_none=True)
