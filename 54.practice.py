class bankaccount:
    def __init__(self, accountno, amount):
        self.accountno=accountno
        self.amount= amount
    def other(self,deposite):
        self.amount += deposite
        print("deposite :",deposite)
        print("balance:",self.amount)
    def others(self,withdraw):
        
        if self.amount >= withdraw: 
            self.amount -= withdraw
            print("withdraw:",withdraw)
            print("balance:",self.amount)
        else:
            print("insufficient")
accountno= input("")
amount= int(input())

s1= bankaccount(accountno,amount)

deposite = int(input())
s1.other(deposite)

withdraw=int(input())
s1.others(withdraw)