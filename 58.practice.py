class student:
    def __init__(self,name,m1,m2,m3):
        self.name= name
        self.m1 = m1
        self.m2 = m2
        self.m3= m3
      
    def calculate_percentage(self,per):
        self.per= ((self.m1+ self.m2+ self.m3)/300)*100
        return self.per

    def grade(self):
        if self.per >= 90:
            print("grade a")
        elif self.per< 90 and self.per>=80:
            print("grade b")
        elif self.per< 80 and self.per >= 70:
            print("grade c")
        elif self.per < 70 and self.per>=60:
            print("grade d")
        else:
            print("fail")

name = input("")
m1= int(input())
m2= int(input())
m3= int(input())
a = student(name, m1, m2, m3)
b= a.calculate_percentage()
print("percentage :",b)
a.grade()