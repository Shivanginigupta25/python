n = input(" ")
u= ""
l=""
d=""
sp=""
for i in n:
    if i.isupper():
        u +=i

    elif i.islower():
        l +=i
    elif i.isdigit():
        d +=i
    else: 
        sp +=i
print("uppercase:", u)
for a in set(u):
    print(a,"=",u.count(a))
print("lowercase:",l)
print("digit:", d)
print("specialcharacter:", sp)