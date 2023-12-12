import time
import multiprocessing

class Watchdog:
    def __init__(self, processes, shutdown_time):
        if shutdown_time <= 0:
            raise ValueError("Časovač musí být déle než 0 sekund!")
        self.shutdown_time = shutdown_time
        self.processes = processes
    
    def start_timer(self):
        for x in range(self.shutdown_time):
            time.sleep(1)
        self.terminate_processes()
    
    def terminate_processes(self):
        for x in self.processes:
            x.kill()
        print("TIME RAN OUT! TERMINATED ALL PROCESSES!")
        