value= int(input())
if value >= 2000:
    discount= value *.10
else:
    discount = 0 

amount= value - discount
gst= amount * 0.18
final= amount + gst
print("Final Amount", final)