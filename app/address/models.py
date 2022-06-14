from sqlalchemy import Column, Integer, String

from .database import Base

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    line1 = Column(String, index=True)
    latitude = Column(String, index=True)
    longitude = Column(String, index=True)
