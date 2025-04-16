from datetime import datetime

from database.sqlite.base import Base
from sqlalchemy import Column, DateTime, String
from utils.timezone import KST


class User(Base):
    __tablename__ = "users"

    user_id = Column(String(64), primary_key=True)
    password = Column(String(64), nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.now(KST), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(KST), nullable=False)
