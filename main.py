from Lesson import Lesson
from Schedule import Schedule
from Classroom import Classroom
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


def get_permutations(input_list):
    for p in permutations(input_list):
        yield list(p)


schedule = Schedule(lesson_days)
schedule.print()
"""
perm_number = 1
for perm in get_permutations(lesson_days[0]):
    perm_number = perm_number + 1
    print(f'----------{perm_number}----------')
    for x in perm:
        print(str(x))
"""
