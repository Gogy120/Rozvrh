class Classroom:
    def __init__(self, name, floor):
        self.name = None
        self.floor = None
        self.set_name(name)
        self.set_floor(floor)

    def set_name(self, name):
        if name is None:
            raise TypeError("Classroom name type is wrong!")
        if len(name) > 3:
            raise ValueError("Classroom name length cannot be bigger than 3!")
        self.name = name

    def set_floor(self, floor):
        if floor is None:
            raise TypeError("Classroom floor type is wrong!")
        if floor < 0:
            raise ValueError("Classroom floor cannot be less than 0!")
        self.floor = floor

    def __str__(self):
        return f'{self.name}, {self.floor}'
