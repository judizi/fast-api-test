import os
from database.sqlite.engine import engine
from database.sqlite.base import Base

import model.user

def init_db():
    Base.metadata.create_all(bind=engine)
    