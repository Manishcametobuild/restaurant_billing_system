class Student:

    def __init__(self, name, course, semester):
        self.name = name
        self.course = course
        self.semester = semester
        self.habits = []
        self.tasks = []
        self.marks = {}

    def add_habit(self, habit):
        self.habits.append(habit)

    def add_task(self, task):
        self.tasks.append(task)

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

