class student:
    def __init__(self):
        self.__marks= 0
    def set(self,marks):
        if 0<=marks<=100 :
            self.__marks= marks
    def get(self):
        return self.__marks
marks= int(input())
b =student()
b.set(marks)
k= b.get()
print("marks",k)