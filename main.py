from Lesson import Lesson
from Schedule import Schedule
from Classroom import Classroom
from Generator import Generator
from Watchdog import Watchdog
import time

if __name__ == '__main__':
    start_time = time.time()
    lesson_days = [
    Lesson("WA", "Pavlát", Classroom("17a", 3), False), Lesson("WA", "Pavlát", Classroom("17a", 3), False),
     Lesson("C", "Studénková", Classroom("24", 4), True), Lesson("A", "Páltiková", Classroom("24", 4), True),
     Lesson("M", "Neugebaureová", Classroom("24", 4), True), None, Lesson("PV", "Mandík", Classroom("18", 3), False),
     Lesson("PV", "Mandík", Classroom("18", 3), False),

    Lesson("M", "Neugebaureová", Classroom("24", 4), True), Lesson("TP", "Nohejl", Classroom("24", 4), True),
     Lesson("PSS", "Molič", Classroom("8a", 2), False), Lesson("PSS", "Molič", Classroom("8a", 2), False),
     Lesson("A", "Páltiková", Classroom("5b", 1), True), Lesson("AM", "Kallmünzer", Classroom("24", 2), True), None,
     Lesson("TV", "Lopocha", Classroom("TV", 0), True),
]
    generator = Generator(lesson_days,4,2_000_0000)
    permutations = generator.generate()
    
    print(f'Total number of permutations: {len(permutations)}')
    end_time = time.time()
    print(f'Elapsed time {end_time - start_time}s')

    """
    set_list = list(permutations)
    for x in set_list:
        for y in x:
            print(y,end="")
        print("")
        """