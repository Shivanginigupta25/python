n = int(input())
for i in range(1, n+1):
    amount= int(input())
    if amount >= 5000:
        discount= amount * 0.25
    elif amount >= 2000:
        discount = amount*.15
    else:
        discount = amount*.05
    print(f"discount {i}each coustere: {discount}")