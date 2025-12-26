unit = int(input())
if unit<=100 :
    bill= unit* 5
elif unit <=200 :
    bill = (unit*5)+ (100- unit)*7
elif unit >200:
    bill = (unit*5)+ (unit* 7)+ (100-unit)*10

print ("Total bill amount", bill)