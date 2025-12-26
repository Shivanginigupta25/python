s= input("enter  ")
v= " "
c= " "
d= " "
sp= " "
for ch in s:
    if ch.isalpha():
       if ch.lower() in "aeiou":
          v += ch
          
       else :

          c += ch
          
    elif ch.isdigit():
      d += ch

    else:
      sp += ch
print("vowerl:", v)
print("consonant:", c)
print("digit:", d)
print("specialdigit:",sp)        
