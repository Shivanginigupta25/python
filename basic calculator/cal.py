def add(num1,num2):
    return num1+ num2
def sub(sum1,num2):
    return num1-num2
def mult(num1,num2):
    return num1*num2
def div(num1, nuum2):
    return num1/num2 
def rem(num1,num2):
    return num1 %num2
def avg(num1, num2):
    return (num1+num2)/2

num1 = float(input())
num2 = float(input())
print("Ypur choice \n 1 addition \n 2 subtraction \n 3 multiplication \n 4 division \n 5 remainder \n 6 average")
ch =  int(input())
if ch==1:
    print(add(num1,num2))

elif ch==2:
    print(sub(num1,num2))
elif ch==3:
    print(mult(num1,num2))
elif ch==4:
    print(div(num1,num2))
elif ch==5:
    print(rem(num1,num2))
elif ch==6:
    print(avg(num1,num2))
