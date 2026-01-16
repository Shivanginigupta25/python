class employee:
    def __init__(self,name,salary):
        self.name= name
        self.salary= salary
        print("name",self.name)
        print("salary:",self.salary)
name= input("")
salary=int(input())
a=employee(name,salary)