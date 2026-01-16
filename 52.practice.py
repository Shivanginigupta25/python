def calculate_bill(amount, tax= 18):
    taxes= amount * 0.18
    final= amount + taxes
    return final
amount = int(input())
result= calculate_bill(amount)
print(f"fimal bill{result}")