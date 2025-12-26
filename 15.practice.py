n= int(input())
d1={ }
d2={ }


for i in range (n):
  key= input(" ")
  value= int(input(" "))
  d1[key]=value

  keys = input(" ")
  values= input(" ")
  d2[keys]=values
  
d1.update(d2)
print (d1)

