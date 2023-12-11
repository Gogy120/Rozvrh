import multiprocessing
import itertools
from Lesson import Lesson
from Schedule import Schedule
from Classroom import Classroom
from Generator import Generator


def get_permutations(day):
    return list(itertools.permutations(day))

if __name__ == "__main__":
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

    pool = multiprocessing.Pool()

    all_permutations = pool.map(get_permutations, lesson_days)

    pool.close()
    pool.join()

    for day, permutations in enumerate(all_permutations):
        print(f'Počet permutací dne číslo {day+1}')
        print(len(permutations))