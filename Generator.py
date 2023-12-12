from itertools import permutations, islice
from multiprocessing import Process, Manager
from Watchdog import Watchdog

class Generator:
    def __init__(self, lesson_days, threads, variants):
        if threads < 1 or threads > 8:
            raise ValueError("Používat lze 1-4 vlákna!")
        if lesson_days is None:
            raise ValueError("List nemůže být prázdný!")
        if variants < 1:
            raise ValueError("Musí být alespoň 1 varianta!")
        self.lesson_days = lesson_days
        self.threads = threads
        self.variants = variants

        manager = Manager() #Nastaveni manageru pro sdilenou promennou mezi procesy (self.results)
        self.result = manager.list()

    def generate_permutations(self):
        #Pred int(self.variants/self.threads) lze dat start permutaci
        self.result.append(list(islice(permutations(self.lesson_days, len(self.lesson_days)), int(self.variants/self.threads))))
    
    def generate(self):
        processes = list()
        for x in range(self.threads):
            process = Process(target=self.generate_permutations)
            processes.append(process)
            process.start()
        for x in processes:
            x.join()

        """
        watchdog = Watchdog(processes,4)
        watchdog.start_timer()
        """
        total_perms = set()
        for perm_lists in self.result:
            for perm in perm_lists:
                total_perms.add(perm)
        return total_perms