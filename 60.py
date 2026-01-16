class employee:
        def __init__(self):
            self.__salary= 0
        def set(self, salary):
            if salary>=0:
              self.__salary=salary

            else:
                print("salary cant be negativw")
        def get(self):
            return self.__salary
salary= int(input())
v= employee()
v.set(salary)

k=v.get()
print("salary",k)


    