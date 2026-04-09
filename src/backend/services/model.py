from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from src.backend.services.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    sensor_type = Column(String)
    valor = Column(Float)
    data = Column(DateTime, default=datetime.utcnow)


