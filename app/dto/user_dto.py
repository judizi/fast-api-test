from constants.response_code import ResponseCode
from constants.response_messages import RESPONSE_MESSAGES
from pydantic import BaseModel


class UserResponse(BaseModel):
    userId: str
    updateAt: str
    createAt: str

get_users_responses = {
    200: {
        "description": "사용자 리스트",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.SUCCESS,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
                    "data": [{"userId": "test", "updateAt": "2023-10-01T00:00:00Z", "createAt": "2023-10-01T00:00:00Z"}], 
                }
            }
        }
    },
    500: {
        "description": "서버 오류",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.SERVER_ERROR,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.SERVER_ERROR),
                }
            }
        }
    },
}

get_user_responses = {
    200: {
        "description": "사용자 조회",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.SUCCESS,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
                    "data": {"userId": "test", "updateAt": "2023-10-01T00:00:00Z", "createAt": "2023-10-01T00:00:00Z"}, 
                }
            }
        }
    },
    404: {
        "description": "사용자 없음",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.NOT_FOUND,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.NOT_FOUND),
                }
            }
        }
    },
    500: {
        "description": "서버 오류",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.SERVER_ERROR,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.SERVER_ERROR),
                }
            }
        }
    },
}

