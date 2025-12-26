d1 ={

}
d2= {}

n= int(input("enter"))
for i in range(n):
    key = input("key ")
    values = input("values ")
    d1.update({key: values})
    n= int(input("enter"))
for i in range(n):
    key = input("key ")
    values = input("values ")
    d2.update({key: values})

d1.update(d2)