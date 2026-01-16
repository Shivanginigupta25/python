class bank:
    def interest(self,principle,time):
      pass
class SBI(bank):
    def interest(self,principle,time):
        rate=5
        return (principle*rate*time)/100
class HDFC(bank):
    def interest(self,principle,time):
        rate= 7
        return (principle*rate*time)/100

principle= int(input())
time= int(input())
s= SBI()
k=s.interest(principle,time)
print("simple",k)
h=HDFC()
g = h.interest(principle,time)
print("interest",g)
