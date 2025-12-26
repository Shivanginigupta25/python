password =input("")

if len(password)>=8 and password.isalnum():
    print("strong")
else:
    print("weak")