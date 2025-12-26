s= input(" ")
v= " "
c= " "
for i in s:
    if i.isalpha():
        if i in "EIOUAaeiou":
            v +=i

        else :
            c +=i
print("vowel",v)
print("consonant",c)