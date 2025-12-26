s = input("")
d={ }

for i in s:

    d[i]= d.get(i,0)+1
for key,value in d.items():
    print(key,"=",value)