n =int(input("no."))
i = 1
while i<= n :
    if i%3 == 0 and i%5 == 0 :
        print(i, end = " ")
    i += 1
print("no divisible by 3 and 5")