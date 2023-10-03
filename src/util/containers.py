from dependency_injector import containers, providers
from repo_connection_db import EngineConnectionDB
from repo_connection_sqs import EngineConnectionSqs
from repo_connection_s3 import EngineConnectionS3
from src.calculator.business.balance_calculation import BalanceCalculation
from src.calculator.repository.files_repository import FilesRepository
from src.orchestrator.business.calculation_process import CalculationProcess
from src.orchestrator.business.reports_making_process import ReportsMakingProcess
from src.orchestrator.controller.sender_messages import SenderMessages
from src.orchestrator.repository.attributes_repository import AttributesRepository
from src.reports_maker.business.make_report import ReportsMaker
from src.reports_maker.repository.reports_repository import ReportsRepository


class Containers(containers.DeclarativeContainer):
    engine_connection_db = providers.Singleton(EngineConnectionDB)
    engine_connection_s3 = providers.Singleton(EngineConnectionS3)
    engine_connection_sqs = providers.Singleton(EngineConnectionSqs)

    attr_repo = providers.Factory(AttributesRepository,
                                  engine_connection=engine_connection_db)
    sender_msg = providers.Factory(SenderMessages,
                                   engine_session=engine_connection_sqs)
    files_repo = providers.Factory(FilesRepository,
                                   engine_connection=engine_connection_db,
                                   engine_bucket_s3=engine_connection_s3)
    reports_repo = providers.Factory(ReportsRepository,
                                     engine_connection=engine_connection_db,
                                     engine_bucket_s3=engine_connection_s3)
    calc_process = providers.Factory(CalculationProcess,
                                     attr_repo=attr_repo,
                                     sender_messages=sender_msg)
    rep_making = providers.Factory(ReportsMakingProcess,
                                   attr_repo=attr_repo,
                                   sender_messages=sender_msg)

    balance_calc = providers.Factory(BalanceCalculation,
                                     files_repo=files_repo)
    reports_maker = providers.Factory(ReportsMaker,
                                      reports_repo=reports_repo)
