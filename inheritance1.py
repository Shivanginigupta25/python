class parent:
    def welcome(self):
        print("welcome students")
class child(parent):
    def accept(self):
        print("hello students ,\n \t welcome to python class")
obj = child()
obj.welcome()
obj.accept()

