class Retail_store_Management:
    store_id= 101
    location="jammu"
    def grocery_section(self):
        ID =int(input("enter id"))
        price=int(input("enter price"))
        print(f"available product id{ID} and price{price}")
    def clothing(self):
        ID =int(input())
        price=int(input())
        
        print(f"available product id{ID} and price{price}")
    def stationary(self):
        ID =int(input())
        price=int(input())
        print(f"available product id{ID} and price{price}")
    def medicines(self):
        number=int(input("how many product u want"))
        list=[]
        list1=[]
        for i in range(number):
            ID =int(input("enterid"))
            list.append(number)
            price=int(input("enter price"))
            list1.append(number)
        print(f"ID: {list[i]}, Price: {list1[i]}")

obj=Retail_store_Management()
print("store_id",obj.store_id)
print( "location" ,obj.location)
ch= int(input("enter your choice for 1 is grocery 2 for clothing 3 for statonary 4 for medicines"))
if ch ==1 :
   obj. grocery_section()
elif ch ==2:
   obj.clothing()
elif ch ==3:
    obj.stationary ()
elif ch ==4:
    obj.medicines ()
else:
   print("wrong choice")