from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base

class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Float)
    description = Column(String)
    humidity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
