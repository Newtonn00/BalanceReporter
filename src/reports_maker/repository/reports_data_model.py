from datetime import datetime
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String, Float

Base = declarative_base()


class ReportsDataModel(Base):
    __tablename__ = 'reports'
    record_id = sa.Column(Integer, primary_key=True)
    user_id = sa.Column(String, nullable=False)
    number_of_week = sa.Column(Integer, nullable=False)
    year = sa.Column(Integer, nullable=False)
    amount = sa.Column(Float, nullable=False)
    file_key = sa.Column(String, nullable=True)
    status = sa.Column(String, nullable=False, default='new')
    calc_date = sa.Column(String, nullable=False)
    store_date = sa.Column(String, nullable=True)

    def __init__(self, record_id: int, user_id: str, number_of_week: int, year: int, amount: float, file_key: str,
                 status: str, calc_date: datetime, store_date: datetime):
        self.record_id = record_id
        self.user_id = user_id
        self.number_of_week = number_of_week
        self.year = year
        self.amount = amount
        self.file_key = file_key
        self.status = status
        self.calc_date = calc_date.strftime("%yyyy-%m-%d %H:%M:%S")
        self.store_date = store_date.strftime("%yyyy-%m-%d %H:%M:%S")