class animal:
    def sound(self):
        print("anmal")


class dog(animal):
    def sound(self):
        print("bark")
class cat(animal):
    def sound(self):
        print("meow")

a= animal()
a.sound()
b= dog()
b.sound()
c= cat()
c.sound()