import random
item= ["Rock", "Paper","Scissor"]
user= input("enter ur choice - Rock , Paper, Scissor \t").capitalize()
comp= random.choice(item)

print(f"your choice  {user}, computer choice {comp}")

if user == comp :
    print("Tie")
elif user == "Rock":
    if comp == "Paper":
        print("computer win")
    else:
        print("You win")

elif user == "Paper":
    if comp == "Scissor":
        print("computer win")
    else:
        print("you win ")
elif user == "Scissor":
    if comp == "Paper" :
        print("you win")
    else:
        print("computer win")

else:
    print("Enter no. according to given choice")