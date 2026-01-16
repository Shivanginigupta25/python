n = int(input())
temp = n
reverse= 0
while temp>0:
    digit= temp%10
    reverse= reverse*10 +digit
    temp //=10
if reverse== n:
    print("pallindrime")
else:
    print("not")