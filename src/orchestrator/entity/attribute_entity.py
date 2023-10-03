from dataclasses import dataclass
from datetime import datetime

from src.orchestrator.controller.processes_names import ProcessesNames


@dataclass
class AttributeEntity():
    process_type_id: ProcessesNames.value
    process_type_name: ProcessesNames.name
    last_start_date: datetime
    work_period: str
    status: str
