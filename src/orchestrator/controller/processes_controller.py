from processes_names import ProcessesNames
from src.orchestrator.business.calculation_process import CalculationProcess
from src.orchestrator.business.reports_making_process import ReportsMakingProcess
from threading import Thread

from src.util.containers import Containers

containers = Containers()
calc_proc = containers.calc_process()
rep_making = containers.rep_making()

class ProcessesController:

    def start_process(self, proc_type: ProcessesNames):
        match proc_type:
            case ProcessesNames.CALCULATOR:
                stream_calc = Thread(target=calc_proc.start_process)
                stream_calc.start()
            case ProcessesNames.REPORTSMAKER:
                stream_rep = Thread(target=rep_making.start_process)
                stream_rep.start()
