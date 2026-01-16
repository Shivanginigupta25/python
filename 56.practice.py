class person:
    def detail(self,name,age):
        self.name= name
        self.age= age
        print(f"name is{self.name}and age {self.age}")
class student(person):
    def detail(self,name,age,marks):
        super().detail(name,age)
        self.marks=marks
      
    def show(self):
      print(f"name is{self.name}and age {self.age} with marks{self.marks}")
name=input("")
age= int(input())
marks= int(input())
s= student()
s.detail(name,age,marks)
s.show()