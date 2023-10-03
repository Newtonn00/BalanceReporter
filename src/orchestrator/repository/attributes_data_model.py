import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, String
from datetime import datetime
Base = declarative_base()


class AttributesDataModel(Base):
    __tablename__ = 'attributes'
    process_type_id = sa.Column(Integer, primary_key=True, )
    process_type_name = sa.Column(String, nullable=False)
    last_start_date = sa.Column(String, dnullable=True)
    work_period = sa.Column(String, default='week')
    status = sa.Column(String, nullable=False, default='working')

    def __init__(self, process_type_id: int, process_type_name: str, last_start_date: datetime,
                 work_period: str, status: str):
        self.process_type_id = process_type_id
        self.process_type_name = process_type_name
        self.last_start_date = last_start_date.strftime("%yyyy-%m-%d %H:%M:%S")
        self.work_period = work_period
        self.status = status
