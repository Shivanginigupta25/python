amount= int(input())
if amount >=5000:
    discount = amount*0.2
elif amount >=3000:
    discount = amount*.15
elif amount >= 1000:
    discount = amount*.1
else :
    print("no amount")

final = amount - discount 
print("Discount amount:" , discount)
print("final:",final)