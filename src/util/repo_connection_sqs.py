from boto3.session import Session
from settings_parser import SettingsParser

class EngineConnectionSqs:
    def __init__(self):
        connection_settings = SettingsParser()
        session = Session(aws_access_key_id=connection_settings.asw_key,
                          aws_secret_access_key=connection_settings.asw_s_key)
        self.sqs = session.resource('sqs')