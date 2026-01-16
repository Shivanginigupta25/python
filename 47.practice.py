a = int(input())
b = int(input())
c = int(input())
d=int(input())
if a>=b and a>=c and a>=d:
    print(a,"is grater")
elif b>=a and b>=c and b>=d:
    print(b,"is greater")
elif d>=a and d>=c and d>=b:
    print(d,"is greater")
else:
    print(c,"is greater")
