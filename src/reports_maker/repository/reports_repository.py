from src.common_entity.reports import ReportsEntity, ReportEntity
from src.reports_maker.repository.reports_data_model import ReportsDataModel
from src.util.repo_connection_db import EngineConnectionDB
from src.util.repo_connection_s3 import EngineConnectionS3


class ReportsRepository:
    def __init__(self, engine_connection: EngineConnectionDB, engine_bucket: EngineConnectionS3):
        self._session = engine_connection.session
        self._bucket_s3 = engine_bucket.bucket_s3

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

    def read_reports_for_creation(self, number_of_week, year):
        reports = ReportsEntity()
        curr_session = self._session()
        reports_data = curr_session.query(ReportsDataModel).filter(ReportsDataModel.year == year,
                                                                   ReportsDataModel.number_of_week == number_of_week)

        for row in reports_data:
            reports.reports.append(self._map_reports_dataclass(data=row))
        curr_session.close()
        return reports

    def write_report(self, weekly_report: ReportsEntity, file_key: str):
        body_message = ""
        for x in weekly_report.reports:
            body_message = body_message + x.user_id+ ';' + str(x.amount) + '\n'

        self._bucket_s3.put_object(Body=body_message,
                                   Key=file_key)

    def update_report_data(self, report_data_to_update):
        curr_session = self._session()
        updated_report_data = ReportsDataModel(
            record_id=report_data_to_update.record_id,
            user_id=report_data_to_update.user_id,
            year=report_data_to_update.year,
            number_of_week=report_data_to_update.number_of_week,
            amount=report_data_to_update.amount,
            file_key=report_data_to_update.file_key,
            status=report_data_to_update.status,
            calc_date=report_data_to_update.calc_date,
            store_date=report_data_to_update.store_date)


        curr_session.merge(updated_report_data)
        curr_session.commit()
        data = curr_session.query(ReportsDataModel).get(report_data_to_update.record_id)
        report_dataclass = self._map_reports_dataclass(data)

        curr_session.close()
        return report_dataclass

