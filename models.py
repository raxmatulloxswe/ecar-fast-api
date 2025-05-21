from enum import Enum

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    text = Column(String)


class Choices(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True)

    choice_text = Column(String)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))

class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_company_related = Column(Boolean)


UZB_REGIONS = [
    ('andijan', 'Andijon'),
    ('bukhara', 'Buxoro'),
    ('ferghana', 'Fargʻona'),
    ('jizzakh', 'Jizzax'),
    ('khorezm', 'Xorazm'),
    ('namangan', 'Namangan'),
    ('navoiy', 'Navoiy'),
    ('kashkadarya', 'Qashqadaryo'),
    ('karakalpakstan', 'Qoraqalpogʻiston Respublikasi'),
    ('samarkand', 'Samarqand'),
    ('sirdarya', 'Sirdaryo'),
    ('surkhandarya', 'Surxondaryo'),
    ('tashkent', 'Toshkent'),
    ('tashkent_city', 'Toshkent shahri'),
]


class Branch(Base):
    __tablename__ = 'branches'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_main = Column(Boolean, default=False)
    address = Column(String, nullable=True)
    region = Column(String, default='tashkent_city')
    phone = Column(String, nullable=True)

