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
    
    def rate_1(self): #Pokud je prvni hodina volna +50b. Pokud je volna hodina jindy +15b.
        total_rating = 0
        for x in range(len(self.lesson_days)):
            if self.lesson_days[x][0] is None:
                total_rating += 50
            for y in range(len(self.lesson_days[x]) - 1):
                if self.lesson_days[x][y+1] is None:
                    total_rating += 15
        return total_rating
    
    def rate_3(self): #Pokud nemusim do jineho patra +10b jinak -5b
        total_rating = 0
        for x in range(len(self.lesson_days)):
            for y in range(len(self.lesson_days[x]) - 1):
                if self.lesson_days[x][y] is not None and self.lesson_days[x][y+1] is not None:
                    floor_difference = self.lesson_days[x][y].classroom.floor - self.lesson_days[x][y+1].classroom.floor
                if floor_difference == 0:
                    total_rating += 10 
                else:
                    total_rating -= 5
        return total_rating
    
    def rate_4(self): #Pokud neni pauza na obed -50b.
        total_rating = 0
        for x in range(len(self.lesson_days)):
            if not self.is_lunch_break(self.lesson_days[x]):
                total_rating -= 50
        return total_rating

    def rate_5(self): #Pokud je vice nez 8 hodin -50b jinak +25b
        total_rating = 0
        for x in self.lesson_days:
            if len(x) > 8:
                total_rating -= 50
            else:
                total_rating += 25
        return total_rating
    
    def rate_6(self):
        total_rating = 0
        for x in range(len(self.lesson_days)):
            for y in range(len(self.lesson_days[x]) -1):
                if self.lesson_days[x][y].is_theory == False and self.lesson_days[x][y+1].is_theory == False:
                    total_rating += 15
        return total_rating
    
    def rate_7(self): #Pokud je matematika prvni hodinu nebo po obede -15b
        total_rating = 0
        for x in range(len(self.lesson_days)):
            if self.lesson_days[x][0].name == "M":
                total_rating -= 15
            for y in range(len(self.lesson_days[x]) -1):
                if (self.lesson_days[x][y] is None and self.lesson_days[x][y+1] is not None) and self.lesson_days[x][y+1].name == "M":
                    total_rating -= 15
        return total_rating                

    
    def is_lunch_break(self, day):
        for x in range(len(day)):
            if day[7] is None or day[6] is None or day[5] is None or day[4] is None:
                return True
        return False