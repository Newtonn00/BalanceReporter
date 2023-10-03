import datetime
import decimal
from dataclasses import dataclass, field
from typing import List


@dataclass
class ReportEntity:
    record_id: int
    user_id: str
    number_of_week: int
    year: int
    amount: decimal
    file_key: str
    status: str
    calc_date: datetime
    store_date: datetime

@dataclass
class ReportsEntity:
    reports: List[ReportEntity] = field(default_factory=list)

