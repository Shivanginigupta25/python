amount= int(input())
if amount%2 == 0:
    discount= amount*.1
else:
    discount= amount*.05

final= amount-discount
print("discount",discount)

print("Final amount",final)
