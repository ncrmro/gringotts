from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from src.database import Base


class API_ACCOUNT(Base):
    __tablename__ = 'api_account'
    id = Column(Integer, primary_key=True)
    api_key = Column(String(80), unique=True)

    def __init__(self, name, api_key):
        self.name = name
        self.api_key = api_key
