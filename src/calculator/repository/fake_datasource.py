import datetime


class FakeDataSource:
    def __init__(self):
        self._data_files = list()
        self._data_files = [{"file_key": "daily_reports/250923.csv", "file_date": datetime.datetime(2023, 9, 25,10, 20, 0)},
        {"file_key": "daily_reports/260923.csv",
                               "file_date": datetime.datetime(2023, 9, 26, 10, 20, 0)},
        {"file_key": "daily_reports/280923.csv", "file_date": datetime.datetime(2023, 9, 28, 10, 20, 0)}]

    def get_data(self):
        return self._data_files
