class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >=40:
            print("pass")
        else:
            print("fail")
s1 = student("rahul", 67)
s1.result()
