email= input("enter the vali mail: ")
k,u,d= 0,0,0
if len(email)>= 6:
    if email[0].isalpha() :
        if ("@" in email ) and (email.count("@")== 1):
            if (email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                           u= 1

                    elif i.isdigit():
                        continue
                    elif i =="_" or i=="." or i=="@":
                        continue
                    else:
                        d= 1
                        
                if k==1 or u==1 or d==1:
                    print("wrong mail5")
                else:
                    print("mail is vali")
            else:
                print("wrong mail4")
        else:
            print("wrong mail3")
    else:
        print("Wrong mail2 ")
else:
    print("Wrong mail1")