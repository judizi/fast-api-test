from constants.response_code import ResponseCode
from constants.response_messages import RESPONSE_MESSAGES
from pydantic import BaseModel


class ApiResponse(BaseModel):
    appName: str
    appVersion: str
    
get_api_responses = {
    200: {
        "description": "API 정보",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.SUCCESS,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
                    "data": {"appName": "FastAPI", "appVersion": "0.1.0"},
                }
            }
        }
    }
}
