class user:
    def __init__(self):
        self.__password= ""
    def set(self,password):
        if len(password)>=6:
            self.__password = password
            return self.__password



    def validate(self,inputs):
        if inputs==self.__password:
            return "valid"
        else:
            return "invalid"

        
            
            
password= input("")
b= user()
k =b.set(password)

print("password",k)
inputs= input("")
l= b.validate(inputs)
print("validation",l)
