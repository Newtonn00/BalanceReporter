import datetime
from src.orchestrator.controller.processes_names import ProcessesNames
from src.orchestrator.entity.attribute_entity import AttributeEntity


class FakeDataSource():
    def __init__(self):
        self._data = [{"process_type": ProcessesNames.CALCULATOR.value,
                       "data": {'id': 1, "process_type": ProcessesNames.CALCULATOR,
                                "start_date": datetime.datetime(2023, 9, 17,
                                                                10, 20, 0),
                                "period": 7,
                                "unit_of_measure": "day",
                                "period_in_sec": 604800}},
                      {"process_type": ProcessesNames.REPORTSMAKER.value,
                       "data": {'id': 1, "process_type": ProcessesNames.REPORTSMAKER,
                                "start_date": datetime.datetime(2023, 9,
                                                                17,
                                                                10, 20, 0),
                                "period": 7,
                                "unit_of_measure": "day",
                                "period_in_sec": 604800}}]

    def get_data(self, proc_type: ProcessesNames):
        return self._data[proc_type.value]

    def set_data(self,attr_entity: AttributeEntity):
        self._data[attr_entity.process_type.value]["data"]["start_date"] = attr_entity.start_date
        self._data[attr_entity.process_type.value]["data"]["period"] = attr_entity.period
        self._data[attr_entity.process_type.value]["data"]["period_in_sec"] = attr_entity.period_in_sec
        self._data[attr_entity.process_type.value]["data"]["unit_of_measure"] = attr_entity.unit_of_measure
