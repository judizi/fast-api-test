from sqlalchemy import create_engine
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../test.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)