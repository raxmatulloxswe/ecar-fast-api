from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import func

from database import Base, DATABASE_URL, engine


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)


class Country(BaseModel):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    short_name = Column(String(5))


class Brand(BaseModel):
    __tablename__ = 'brand'

    ind = Column(Integer, primary_key=True)
    title = Column(String(255))
    country_id = Column(Integer, ForeignKey('country.id'))
    country = relationship('Country')

Base.metadata.create_all(bind=engine)