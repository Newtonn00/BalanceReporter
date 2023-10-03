from src.orchestrator.entity.attribute_entity import AttributeEntity
from boto3.session import Session

from src.util.repo_connection_sqs import EngineConnectionSqs


class SenderMessages:

    def __init__(self, engine_session: EngineConnectionSqs):
        sqs = engine_session.sqs
        self._queue = sqs.get_queue_by_name(QueueName='sqs4reporting')

    def send_calc_message_to_queue(self, attr_entity: AttributeEntity, number_of_week, year):
        message_body = '{"process_type": ' + str(
            attr_entity.process_type.value) + ',"action": "go", "number_of_week: ' + str(
            number_of_week) + ',"year: "' + str(year) + '}'
        response = self._queue.send_message(MessageBody=message_body)

    def send_report_message_to_queue(self, attr_entity: AttributeEntity, number_of_week, year):
        message_body = '{"process_type": ' + str(
            attr_entity.process_type.value) + ',"action": "go", "number_of_week: ' + str(
            number_of_week) + ',"year: "' + str(year) + '}'
        response = self._queue.send_message(MessageBody=message_body)
