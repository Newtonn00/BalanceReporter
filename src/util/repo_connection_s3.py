from boto3.session import Session
from settings_parser import SettingsParser


class EngineConnectionS3:
    def __init__(self):
        connection_settings = SettingsParser()
        session = Session(aws_access_key_id=connection_settings.asw_key,
                          aws_secret_access_key=connection_settings.asw_s_key)
        s3_session = session.resource('s3')
        self.bucket_s3 = s3_session.Bucket(connection_settings.s3_bucket)