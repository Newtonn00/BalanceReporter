import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import String
from datetime import datetime

Base = declarative_base()


class DailyFilesModel(Base):
    __tablename__ = 'daily_files'
    file_key = sa.Column(String, primary_key=True)
    record_date = sa.Column(String, nullable=False)

    def __init__(self, file_key: str, record_date: datetime):
        self.file_key = file_key
        self.store_date = record_date.strftime("%yyyy-%m-%d %H:%M:%S")
