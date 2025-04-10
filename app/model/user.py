from database.sqlite.base import Base
from sqlalchemy import Column, DateTime, String
from datetime import datetime
from utils.timezone import KST

class User(Base):
    __tablename__ = "users"

    user_id = Column(String(64), primary_key=True)
    user_password = Column(String(64), primary_key=True)
    updated_at = Column(DateTime(timezone=True), default=datetime.now(KST), primary_key=False, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(KST), primary_key=False, nullable=False)
