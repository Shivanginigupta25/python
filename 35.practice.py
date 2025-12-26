n= int(input())
fee= int(input())
sum= 0
for i in range(1,n+1):
    marks= int(input())
    sum += marks
per= (sum/(n*100))*100
if per >=70:
    dis= fee * .1
else:
    dis =0
    print("no discount")
final= fee- dis
print("percentage is ",per)
print("discountis",dis)
print("fee is ", final)
