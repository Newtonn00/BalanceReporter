from datetime import datetime

from src.calculator.entity.daily_files import DailyFiles, DailyFile
from src.calculator.repository.daily_files_data_model import DailyFilesModel
from src.calculator.repository.reports_data_model import ReportsDataModel
from src.common_entity.reports import ReportEntity
from src.util.repo_connection_db import EngineConnectionDB
from src.util.repo_connection_s3 import EngineConnectionS3


class FilesRepository:
    def __init__(self, engine_connection: EngineConnectionDB, engine_bucket_s3: EngineConnectionS3):
        self._session = engine_connection.session
        self._s3_bucket = engine_bucket_s3.bucket_s3

    def _map_file_dataclass(self, data) -> DailyFile:
        file_dataclass = DailyFile(
            file_key=data["file_key"],
            record_date=data["record_date"]
        )
        return file_dataclass

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

    def read_daily_files_data(self, date_begin: datetime.date, date_end: datetime.date):
        daily_files = DailyFiles()
        curr_session = self._session()
        data = curr_session.query(DailyFilesModel).filter(date_begin <= datetime.strptime(DailyFilesModel.record_date,
                                                                                     "%yyyy-%m-%d %H:%M:%S") < date_end)
        for row in data:
            daily_files.files.append(self._map_file_dataclass(data=row))
        curr_session.close()
        return daily_files

    def read_daily_balances(self, file_keys) -> dict:
        lines = []
        bucket = self._s3_bucket
        for x in file_keys:
            obj = bucket.Object(key=x)
            response = obj.get()
            for y in response[u'Body'].read().decode('Windows−1251').splitlines():
                lines.append(y)

        return self.convert_str_to_dict(lines)

    def convert_str_to_dict(self, data_for_convert) -> dict:
        lines_dict = dict()
        for i in range(0, len(data_for_convert)):
            record_data = data_for_convert[i].split(";")
            rec_dict = dict(user_id=record_data[0], amount=record_data[1], currency=record_data[2])
            lines_dict[str(i)] = rec_dict
        return lines_dict

    def write_weekly_reports_data(self, weekly_data: ReportEntity):
        curr_session = self._session()
        report = ReportsDataModel(
            record_id=weekly_data.record_id,
            user_id=weekly_data.user_id,
            year=weekly_data.year,
            number_of_week=weekly_data.number_of_week,
            amount=weekly_data.amount,
            file_key=weekly_data.file_key,
            status=weekly_data.status,
            calc_date=weekly_data.calc_date,
            store_date=weekly_data.store_date)

        curr_session.add(report)
        curr_session.commit()

        data = curr_session.query(ReportsDataModel).get(report.record_id)
        report_dataclass = self._map_reports_dataclass(data=data)
        curr_session.close()
        return report_dataclass
