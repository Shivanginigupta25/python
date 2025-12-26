def fun1(n):
  
    if n==0:
        return 1
    return n*fun1(n-1)

n= int(input(""))
print(fun1(n))
        