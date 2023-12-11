from itertools import permutations
import multiprocessing

class Generator:
    def __init__(self, lesson_days):
        self.lesson_days = lesson_days
    
    def get_permutations(self,list):
        for p in permutations(list):
            yield set(p)

    def generate(self):
        processes = []
        for x in range(len(self.lesson_days)):
            p = multiprocessing.Process(target=self.get_permutations(self.lesson_days[x]))
            processes.append(p)
        for x in processes:
            x.start()
        for x in processes:
            x.join()
