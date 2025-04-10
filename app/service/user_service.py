from constants.response_code import ResponseCode
from constants.response_messages import RESPONSE_MESSAGES
from model.user import User
from sqlalchemy.orm import Session
from utils.response import create_response_dto


def get_user_list(skip: int, limit: int, db: Session) -> dict:
    try:
        users = db.query(User).offset(skip).limit(limit).all()
        return create_response_dto(
            code=ResponseCode.SUCCESS,
            message=RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
            data=users
        )
    except Exception as e:
        return create_response_dto(
            code=ResponseCode.SERVER_ERROR,
            message=str(e),
        )
    
def get_user_by_id(user_id: str, db: Session) -> dict:
    try:
        user = db.query(User).filter(User.user_id == user_id).first()
    except Exception as e:
        return create_response_dto(
            code=ResponseCode.SERVER_ERROR,
            message=str(e),
        )

    if not user:
        return create_response_dto(
            code=ResponseCode.NOT_FOUND,
            message=RESPONSE_MESSAGES.get(ResponseCode.NOT_FOUND),
        )
    
    return user
