from src.reports_maker.repository.reports_repository import ReportsRepository


class ReportsMaker:
    def __init__(self, reports_repo: ReportsRepository):
        self._reports_repo = reports_repo

    def make_report(self, number_of_week, year):
        data_for_making_report = self._reports_repo.read_reports_for_creation(number_of_week, year)
        file_key = "weekly_reports/" + str(year) + str(number_of_week) + ".csv"
        self._save_report(data_for_making_report, file_key)

    def _save_report(self, report_data, file_key: str):

        self._reports_repo.write_report(report_data, file_key)
        self._reports_repo.update_report_data(report_data_to_update=report_data)
