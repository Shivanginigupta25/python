class account:
    def __init__(self,amount):
        self.amount= amount
class savingaccount(account):
    def __init__(self,amount,interest):
        super().__init__(amount)
        self.interest = interest
    
    def show(self):
        print(f"total amout{self.amount} anf interest is{self.interest}")

amount= int(input())
interest= int(input())
o = savingaccount(amount,interest)
o.show()
