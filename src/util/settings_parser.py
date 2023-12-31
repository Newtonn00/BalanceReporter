import configparser
import os
from settings_error import SettingsError


class SettingsParser:
    db_user_name: str
    db_name: str
    db_host: str
    db_password: str
    asw_key: str
    asw_s_key: str
    s3_bucket: str

    def __init__(self):

        _settings_file_exists = True
        config = configparser.ConfigParser()
        if os.path.exists(os.environ.get('WORKDIR')+'/settings.ini') is False:
            _settings_file_exists = False
        else:
            config.read(os.environ.get('WORKDIR')+'/settings.ini')

        if (os.environ.get('DB_NAME') == '' or os.environ.get('DB_NAME') is None) and _settings_file_exists and config.has_option('db','db_name'):
            self.db_name = config['db']['db_name']
        else:
            self.db_name = os.environ.get('DB_NAME')

        if (os.environ.get('DB_HOST') == '' or os.environ.get('DB_HOST') is None) and _settings_file_exists and config.has_option('db','db_host'):
            self.db_host = config['db']['db_host']
        else:
            self.db_host = os.environ.get('DB_HOST')

        if (os.environ.get('DB_USER_NAME') == '' or os.environ.get('DB_USER_NAME') is None) and _settings_file_exists and config.has_option('db','db_user_name'):
            self.db_user_name = config['db']['db_user_name']
        else:
            self.db_user_name = os.environ.get('DB_USER_NAME')

        if (os.environ.get('DB_PASSWORD') == '' or os.environ.get('DB_PASSWORD') is None) and _settings_file_exists and config.has_option('db','db_password'):
            self.db_password = config['db']['db_password']
        else:
            self.db_password = os.environ.get('DB_PASSWORD')

        if (os.environ.get('ASW_KEY') == '' or os.environ.get(
                'ASW_KEY') is None) and _settings_file_exists and config.has_option('asw', 'asw_key'):
            self.asw_key = config['asw']['asw_key']
        else:
            self.asw_key = os.environ.get('ASW_KEY')

        if (os.environ.get('ASW_S_KEY') == '' or os.environ.get(
                'ASW_S_KEY') is None) and _settings_file_exists and config.has_option('asw', 'asw_s_key'):
            self.asw_s_key = config['asw']['asw_s_key']
        else:
            self.asw_s_key = os.environ.get('ASW_S_KEY')

        if (os.environ.get('S3_BUCKET') == '' or os.environ.get(
                'S3_BUCKET') is None) and _settings_file_exists and config.has_option('asw', 's3_bucket'):
            self.s3_bucket = config['asw']['s3_bucket']
        else:
            self.s3_bucket = os.environ.get('S3_BUCKET')

        if (self.db_name == '') or (self.db_user_name == '') or (self.db_host == '') or (self.db_password == ''):
            raise SettingsError()
