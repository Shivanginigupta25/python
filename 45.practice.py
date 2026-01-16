classes =int(input())
total_class= int(input())
attendence= (classes/total_class)*100
if attendence >= 75:
    print("Allowed")
else:
    print("Not Allowed")