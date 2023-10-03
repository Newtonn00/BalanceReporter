import datetime
from dataclasses import dataclass, field
from typing import List


@dataclass
class DailyFile:
    file_key: str
    record_date: datetime

@dataclass
class DailyFiles:
    files: List[DailyFile] = field(default_factory=list)