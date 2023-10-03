import datetime
import time
from src.orchestrator.controller.processes_names import ProcessesNames
from src.orchestrator.controller.sender_messages import SenderMessages
from src.orchestrator.entity.attribute_entity import AttributeEntity
from src.orchestrator.repository.attributes_repository import AttributesRepository


class ReportsMakingProcess:

    def __init__(self, attr_repo: AttributesRepository, sender_messages: SenderMessages):
        self._sender_messages = sender_messages
        self._attr_rep = attr_repo
        self._attr_entity = self.get_attributes()
        self._last_start_date = self._attr_entity.last_start_date
        self._message_sent = False

    def get_attributes(self) -> AttributeEntity:
        return self._attr_rep.read_attribute(proc_type=ProcessesNames.REPORTSMAKER)

    def store_new_date(self, new_date: datetime):
        self._attr_entity.last_start_date = new_date
        self._attr_rep.update_attribute(self._attr_entity)

    def start_process(self):
        print("ReportMaker started")
        print(self._last_start_date)

        while 1 == 1:
            new_start_date = datetime.datetime.now()

            if int(datetime.datetime.now().strftime("%H")) > int(new_start_date.strftime("%H")) + 4:
                self._message_sent = False
            if len(self._attr_rep.read_reports_for_create()) > 0 and not self._message_sent:
                self.store_new_date(new_start_date)
                self._last_start_date = new_start_date
                self._message_sent = True
                self.send_message(new_start_date.strftime("%W"), new_start_date.strftime("%H"))

            time.sleep(10)

    def send_message(self, number_of_week, year):
        self._sender_messages.send_report_message_to_queue(attr_entity=self._attr_entity, number_of_week=number_of_week,
                                                           year=year)
