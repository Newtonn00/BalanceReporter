import datetime
import time
from datetime import date, timedelta

from src.orchestrator.repository.attributes_repository import AttributesRepository
from src.orchestrator.controller.processes_names import ProcessesNames
from src.orchestrator.controller.sender_messages import SenderMessages
from src.orchestrator.entity.attribute_entity import AttributeEntity


class CalculationProcess:

    def __init__(self,attr_repo: AttributesRepository,sender_messages:SenderMessages):
        self._sender_messages = sender_messages
        self._attr_rep = attr_repo
        self._attr_entity = self.get_attributes()
        self._last_start_date = self._attr_entity.last_start_date

    def get_attributes(self) -> AttributeEntity:

        return self._attr_rep.read_attribute(proc_type=ProcessesNames.CALCULATOR)

    def store_new_date(self, new_date: datetime):
        self._attr_entity.last_start_date = new_date
        self._attr_rep.update_attribute(self._attr_entity)

    def start_process(self):
        print("Calculator started")
        print(self._last_start_date)

        while 1 == 1:
            new_start_date = datetime.datetime.now()
            if datetime.datetime.now().strftime("%w") == 1 and self._start_date.strftime("%W") != 1:
                self.store_new_date(new_start_date)
                self._last_start_date = new_start_date
                number_of_week = new_start_date.strftime("%W")
                year = new_start_date.strftime("%y")
                self.send_message(number_of_week, year)
            time.sleep(10)

    def send_message(self, number_of_week, year):
        self._sender_messages.send_calc_message_to_queue(attr_entity=self._attr_entity, number_of_week=number_of_week, year=year)

