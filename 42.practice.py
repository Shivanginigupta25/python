cost= int(input())
sell =int(input())
if sell > cost:
    print("profit")
    profit= sell-cost
    print("profit",profit)
elif cost>sell:
    print("lost")
    lost= cost-profit
    print("loss ",lost)

else:
    print("nolost")
