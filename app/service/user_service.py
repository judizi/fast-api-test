from constants.response_code import ResponseCode
from constants.response_messages import RESPONSE_MESSAGES
from dto.response_dto import ResponseModel
from dto.user_dto import UserCreate, UserResponse
from model.user import User
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from utils.hash import hash_password
from utils.response import create_response_dto


def get_user_data_list(skip: int, limit: int, db: Session) -> ResponseModel:
    try:
        stmt = select(User).offset(skip).limit(limit)
        user_datas = db.execute(stmt).scalars().all()
        
        user_response = [UserResponse.model_validate(user_data) for user_data in user_datas]
        return create_response_dto(
            code=ResponseCode.SUCCESS,
            message=RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
            data=user_response
        )
    
    except Exception as e:
        return create_response_dto(
            code=ResponseCode.SERVER_ERROR,
            message=str(e),
        )
    
def get_user_data_by_id(user_id: str, db: Session) -> ResponseModel:
    try:
        stmt = select(User).where(User.user_id == user_id)
        user_data = db.execute(stmt).scalars().first()

    except Exception as e:
        return create_response_dto(
            code=ResponseCode.SERVER_ERROR,
            message=str(e),
        )

    if not user_data:
        return create_response_dto(
            code=ResponseCode.NOT_FOUND,
            message=RESPONSE_MESSAGES.get(ResponseCode.NOT_FOUND),
        )
    
    user_response = UserResponse.model_validate(user_data)
    
    return create_response_dto(
        code=ResponseCode.SUCCESS,
        message=RESPONSE_MESSAGES.get(ResponseCode.SUCCESS),
        data=user_response
    )

def insert_user_data(user: UserCreate, db: Session) -> ResponseModel:
    try:
        user_data = User(
            user_id=user.userId,
            email=user.email,
            password=hash_password(user.password)
        )

        db.add(user_data)
        db.commit()
        db.refresh(user_data)

        user_response = UserResponse.model_validate(user_data)

        return create_response_dto(
            code=ResponseCode.CREATED,
            message=RESPONSE_MESSAGES.get(ResponseCode.CREATED),
            data=user_response
        )
    
    except IntegrityError as ie:
        db.rollback()
        return create_response_dto(
            code=ResponseCode.DUPLICATE_RESOURCE,
            message=RESPONSE_MESSAGES.get(ResponseCode.DUPLICATE_RESOURCE),
        )
    
    except Exception as e:
        db.rollback()
        return create_response_dto(
            code=ResponseCode.SERVER_ERROR,
            message=str(e),
        )
