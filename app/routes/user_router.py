from typing import List

from controllers.user_controller import get_user, get_users, insert_user
from database.sqlite.session import get_db
from dto.response_dto import ResponseModel
from dto.user_dto import (UserCreate, UserResponse, get_user_responses,
                          get_users_responses, insert_user_responses)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get(
    path="/", 
    response_model=ResponseModel[List[UserResponse]],
    responses=get_users_responses
)
def read_users(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    return get_users(skip, limit, db)

@router.get(
    path="/{user_id}", 
    response_model=ResponseModel[UserResponse],
    responses=get_user_responses
)
def read_user(user_id: str="test", db: Session=Depends(get_db)):
    return get_user(user_id, db)

@router.post(
    path="/{user_id}", 
    status_code=201,
    response_model=ResponseModel[UserResponse],
    responses=insert_user_responses
)
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    return insert_user(user, db)
