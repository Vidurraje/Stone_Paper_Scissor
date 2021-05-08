import random
print("*"*40,"Welcome to Stone Paper Scissor","*"*40)
lst = ["stone", "paper","scissor"]
try:
    while True:
        value = random.choice(lst)
        x = input("Enter your choice between \nstone \npaper  \nscissor \nEnter choice: ")
        user_input=x.lower()
        print("*" * 100)
        if user_input=="stone" or user_input=="paper" or user_input=="scissor":
            print("Computer entered:- ", value)
            if user_input==value:
                print("*"*45, " GAME DRAW ","*"*45)
            elif (user_input=="stone" and value=="paper") or (user_input=="scissor" and value=="stone") or (user_input=="paper" and value=="scissor") :
                 print("*" * 45, " COMPUTER WON THIS GAME ", "*" * 45)
            else:
                print("*" * 45, " You won this game  ", "*" * 45)
        else:
            print(" Invald Input ")
            print("*" * 100)
        x=input("Do you want to continue? press (Y/N):  ")
        if x=="Y" or x=="y":
            continue
        else:
            break
except:
    print("Invalid Input")
