import json
from time import sleep

from boto3 import Session
from src.orchestrator.controller.processes_names import ProcessesNames
from src.calculator.business.balance_calculation import BalanceCalculation
from src.util.containers import Containers

containers = Containers()
sqs = containers.engine_connection_sqs().sqs
bal_calc = containers.balance_calc()
queue = sqs.get_queue_by_name(QueueName='sqs4reporting')
max_queue_messages = 5
message_bodies = []
while 1 == 1:

    for message in queue.receive_messages(
            MaxNumberOfMessages=max_queue_messages):
        # process message body
        messages_to_delete = []
        body = json.loads(message.body)
        print(body["process_type"])
        if body["process_type"] == ProcessesNames.CALCULATOR.value:
            # add message to delete#
            print("message found")
            bal_calc.calculate_balance(body["number_of_week"], body["year"])
            messages_to_delete.append({
                'Id': message.message_id,
                'ReceiptHandle': message.receipt_handle
            })
        # if you don't receive any notifications the
        # messages_to_delete list will be empty
        if len(messages_to_delete) == 0:
            break
        # delete messages to remove them from SQS queue
        # handle any errors
        else:
            delete_response = queue.delete_messages(
                Entries=messages_to_delete)
        sleep(30)