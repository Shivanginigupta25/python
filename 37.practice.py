amount = int(input())
withdraw= int(input())
if withdraw %100 ==0 and withdraw < amount:
    balance = amount-withdraw
    print(balance)
    print("transaction is successful")
else:
    print("Transacton is unsucessfulS")