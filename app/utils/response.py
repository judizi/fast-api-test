from typing import Optional

from dto.response_dto import ResponseModel, T
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def create_response(http_code: int, content: ResponseModel) -> JSONResponse:
    return JSONResponse(
        status_code=http_code,
        content=jsonable_encoder(content.model_dump(exclude_none=True))
    )

def create_response_dto(code: int, message: str, data: Optional[T]=None) -> ResponseModel:
    if data is None:
        return ResponseModel(code=code, message=message)
    return ResponseModel(code=code, message=message, data=data)
