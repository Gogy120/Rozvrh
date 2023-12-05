from Classroom import Classroom


class Lesson:
    def __init__(self, name, teacher, classroom, is_theory):
        self.name = None
        self.teacher = None
        self.classroom = None
        self.is_theory = None
        self.set_name(name)
        self.set_teacher(teacher)
        self.set_classroom(classroom)
        self.set_is_theory(is_theory)

    def set_teacher(self, teacher):
        if teacher is None:
            raise TypeError("Lesson teacher type is wrong!")
        self.teacher = teacher

    def set_name(self, name):
        if name is None:
            raise TypeError("Lesson name type is wrong!")
        if len(name) > 3:
            raise ValueError("Lesson name length cannot be bigger than 3!")
        self.name = name.upper()

    def set_classroom(self, classroom):
        if classroom is None:
            raise TypeError("Lesson classroom type is wrong!")
        self.classroom = classroom

    def set_is_theory(self, is_theory):
        if is_theory is None:
            raise TypeError("Lesson is_theory type is wrong!")
        self.is_theory = is_theory

    def __str__(self):
        return f'[{self.name}]'
