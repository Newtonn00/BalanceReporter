from src.common_entity.reports import ReportEntity
from src.orchestrator.controller.processes_names import ProcessesNames
from src.orchestrator.entity.attribute_entity import AttributeEntity
from src.orchestrator.repository.attributes_data_model import AttributesDataModel
from src.orchestrator.repository.reports_data_model import ReportsDataModel
from src.util.repo_connection_db import EngineConnectionDB


class AttributesRepository:

    def __init__(self, engine_connection: EngineConnectionDB):

        self._session = engine_connection.session

    def _map_attr_dataclass(self, data) -> AttributeEntity:
        attr_dataclass = AttributeEntity(
            process_type_id=data["process_type_id"],
            process_type_name=data["process_type_name"],
            last_start_date=data["last_start_date"],
            work_period=data["work_period"],
            status=data["status"])
        return attr_dataclass

    def _map_reports_dataclass(self, data) -> ReportEntity:
        report_dataclass = ReportEntity(
            record_id=data["record_id"],
            user_id=data["user_id"],
            number_of_week=data["number_of_week"],
            year=data["year"],
            amount=data["amount"],
            file_key=data["file_key"],
            status=data["status"],
            calc_date=data["calc_date"],
            store_date=data["store_data"]
        )
        return report_dataclass

    def read_attribute(self, proc_type: ProcessesNames) -> AttributeEntity:
        curr_session = self._session()
        data = curr_session.query(AttributesDataModel).get(proc_type.value)
        attribute_dataclass = AttributesRepository._map_attr_dataclass(self, data=data)
        curr_session.close()
        return attribute_dataclass

    def read_reports_for_create(self):
        curr_session = self._session()
        data = curr_session.query(ReportsDataModel).filter(ReportsDataModel.status == "new")
        reports_dataclass = AttributesRepository._map_reports_dataclass(self, data=data)
        curr_session.close()
        return reports_dataclass

    def update_attribute(self, attr_entity: AttributeEntity):
        curr_session = self._session()
        updated_attribute = AttributesDataModel(process_type_id=attr_entity.process_type_id,
                                                process_type_name=attr_entity.process_type_name,
                                                last_start_date=attr_entity.last_start_date,
                                                work_period=attr_entity.work_period,
                                                status=attr_entity.status)
        updated_attribute.process_type_id = attr_entity.process_type_id
        curr_session.merge(updated_attribute)
        curr_session.commit()
        data = curr_session.query(AttributesDataModel).get(attr_entity.process_type_id)
        attr_dataclass = self._map_attr_dataclass(data)

        curr_session.close()
        return attr_dataclass
