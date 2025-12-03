class Student:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("student name", self.name)

s = Student("Harry")
s.show()
