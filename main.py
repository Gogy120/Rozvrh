from Lesson import Lesson
from Schedule import Schedule
from Classroom import Classroom
from Generator import Generator
from multiprocessing import Pool
from itertools import permutations

lesson_days = [
    [Lesson("WA", "Pavlát", Classroom("17a", 3), False), Lesson("WA", "Pavlát", Classroom("17a", 3), False),
     Lesson("C", "Studénková", Classroom("24", 4), True), Lesson("A", "Páltiková", Classroom("24", 4), True),
     Lesson("M", "Neugebaureová", Classroom("24", 4), True), None, Lesson("PV", "Mandík", Classroom("18", 3), False),
     Lesson("PV", "Mandík", Classroom("18", 3), False)],

    [Lesson("M", "Neugebaureová", Classroom("24", 4), True), Lesson("TP", "Nohejl", Classroom("24", 4), True),
     Lesson("PSS", "Molič", Classroom("8a", 2), False), Lesson("PSS", "Molič", Classroom("8a", 2), False),
     Lesson("A", "Páltiková", Classroom("5b", 1), True), Lesson("AM", "Kallmünzer", Classroom("24", 2), True), None,
     Lesson("TV", "Lopocha", Classroom("TV", 0), True)],
]



schedule = Schedule(lesson_days)
print(schedule.rate_1())

if __name__ == '__main__':
    g = Generator(lesson_days)
    g.generate()
