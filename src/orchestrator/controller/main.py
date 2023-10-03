import json

from boto3.session import Session

from processes_controller import ProcessesController
from processes_names import ProcessesNames
from src.util.containers import Containers

if __name__ == '__main__':
    container = Containers()
    processes_controller = ProcessesController()
    ProcessesController.start_process(processes_controller, ProcessesNames.CALCULATOR)
    ProcessesController.start_process(processes_controller, ProcessesNames.REPORTSMAKER)
