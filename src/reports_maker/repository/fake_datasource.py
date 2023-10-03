import datetime


class FakeDataSource:
    def __init__(self):
        self._data_files = list()
        self._data_files = [
            {"user_id": "opetrov", "number_of_week": 17, "year": 2023, "amount": -100, "file_key": None, "stored": False,
             "calc_date": datetime.datetime(2023, 9, 25, 10, 20, 0), "strored_date": None},
            {"user_id": "oivanov", "number_of_week": 17, "year": 2023, "amount": 200.0, "file_key": None,
             "stored": False, "calc_date": datetime.datetime(2023, 9, 25, 10, 10, 0), "strored_date": None},
            {"user_id": "ssemenov", "number_of_week": 17, "year": 2023, "amount": 14.6,
             "file_key": "weeklyreports/16weeklyreport.csvf", "stored": True,
             "calc_date": datetime.datetime(2023, 9, 25, 10, 25, 0),
             "strored_date": datetime.datetime(2023, 12, 25, 10, 25, 0)},
            {"user_id": "rmartint", "number_of_week": 17, "year": 2023, "amount": -10.4, "file_key": None,
             "stored": False, "calc_date": datetime.datetime(2023, 9, 25, 10, 25, 0), "strored_date": None}]

    def get_data(self):
        return self._data_files
