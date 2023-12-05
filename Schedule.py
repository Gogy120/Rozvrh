class Schedule:
    def __init__(self, lesson_days):
        self.lesson_days = None
        self.set_lesson_days(lesson_days)

    def set_lesson_days(self, lesson_days):
        if lesson_days is None:
            raise TypeError("Schedule lesson_days type is wrong!")
        self.lesson_days = lesson_days

    def print(self):
        days_in_week = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
        for x in range(len(self.lesson_days)):
            print(f'----------{days_in_week[x]}----------')
            for y in range(len(self.lesson_days[x])):
                if self.lesson_days[x][y] is not None:
                    print(self.lesson_days[x][y], end="")
                else:
                    print("[Volno]", end="")
            print("")
