import datetime

from src.common_entity.reports import WeeklyReport, ReportEntity
from src.calculator.repository.files_repository import FilesRepository


class BalanceCalculation:
    def __init__(self, files_repo: FilesRepository):
        self._weekly_entity = WeeklyReport
        self._files_repo = files_repo

    def calculate_balance(self, number_of_week, year):
        start_week_date = self.get_date_from_week_number(number_of_week, year)

        end_week_date = start_week_date + datetime.timedelta(days=7)

        file_keys_list = self._files_repo.read_daily_files_data(date_begin=start_week_date,
                                                                date_end=end_week_date)
        balances_list = self._files_repo.read_daily_balances(file_keys=file_keys_list)
        weekly_data = self.calculate_weekly_amounts(daily_balances_list=balances_list)

        for x, y in weekly_data.items():
            self._files_repo.write_weekly_reports_data(weekly_data=self.map_to_entity(x, y))

    def calculate_weekly_amounts(self, daily_balances_list):
        weekly_balances = dict()
        for x in daily_balances_list.values():

            if x["user_id"] in weekly_balances.keys():
                weekly_balances[x["user_id"]] = weekly_balances[x["user_id"]] + float(x["amount"])
            else:
                weekly_balances[x["user_id"]] = float(x["amount"])

        return weekly_balances

    def map_to_entity(self, user_id: str, amount: float) -> WeeklyReport:
        self._weekly_entity = ReportEntity(record_id=0,user_id=user_id, amount=amount,
                                           calc_date=datetime.datetime.now(), year=int(str(datetime.date.year)),
                                           number_of_week=int(datetime.datetime.now().strftime('%W')), status="new",
                                           store_date=None, file_key="")

        return self._weekly_entity

    def get_date_from_week_number(self, week_number, year):
        return datetime.datetime.strptime(f'{year}-{week_number}-1', "%Y-$W-$w").date()
