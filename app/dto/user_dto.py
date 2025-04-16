from datetime import datetime
from http import HTTPStatus


from constants.response_code import ResponseCode
from constants.response_messages import RESPONSE_MESSAGES
from pydantic import BaseModel, ConfigDict, Field, field_serializer


class UserResponse(BaseModel):
    userId: str = Field(alias="user_id")
    email: str = Field(alias="email")
    updatedAt: datetime = Field(alias="updated_at")
    createdAt: datetime = Field(alias="created_at")

    model_config = ConfigDict(
        orm_mode=True,
        populate_by_name=True,
        from_attributes=True,
    )

    @field_serializer('updatedAt', 'createdAt')
    def serialize_datetime(self, dt: datetime, _info) -> str:
        return dt.strftime('%Y-%m-%d %H:%M:%S')

class UserCreate(BaseModel):
    userId: str = "test"
    email: str = "test@test.com"
    password: str = "test1234"

get_users_responses = {
    HTTPStatus.OK: {
        "description": "사용자 리스트",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.SUCCESS,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
                    "data": [
                        {
                            "userId": "test", 
                            "email": "test@test.com", 
                            "updatedAt": "2023-10-01T00:00:00", 
                            "createdAt": "2023-10-01T00:00:00"}], 
                }
            }
        }
    },
    HTTPStatus.INTERNAL_SERVER_ERROR: {
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
    HTTPStatus.OK: {
        "description": "사용자 조회",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.SUCCESS,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
                    "data": {
                        "userId": "test", 
                        "email": "test@test.com", 
                        "updatedAt": "2023-10-01T00:00:00", 
                        "createdAt": "2023-10-01T00:00:00"
                    }, 
                }
            }
        }
    },
    HTTPStatus.NOT_FOUND: {
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
    HTTPStatus.INTERNAL_SERVER_ERROR: {
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

insert_user_responses = {
    HTTPStatus.CREATED: {
        "description": "사용자 추가",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.CREATED,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.CREATED),
                    "data": {
                        "userId": "test", 
                        "email": "test@test.com", 
                        "updatedAt": "2023-10-01T00:00:00", 
                        "createdAt": "2023-10-01T00:00:00"
                    }, 
                }
            }
        }
    },
    HTTPStatus.CONFLICT: {
        "description": "사용자 id, email 중복",
        "content": {
            "application/json": {
                "example": {
                    "code": ResponseCode.DUPLICATE_RESOURCE,
                    "message": RESPONSE_MESSAGES.get(ResponseCode.DUPLICATE_RESOURCE),
                }
            }
        }
    },
    HTTPStatus.INTERNAL_SERVER_ERROR: {
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

