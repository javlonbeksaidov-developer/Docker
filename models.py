from sqlalchemy import Column, Float, Integer, String

from database import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255))
    price = Column(Float)
    amount = Column(Integer)
