def calculate_discount(amount):
    if amount >=5000:
        discount = amount*.2
    elif amount >=2000:
        discount = amount*.1

    else:
        discount = amount*0
        print("no discount")
    
    return discount
amount = int (input())
result= calculate_discount(amount)
print(f"discount amount is{result}")