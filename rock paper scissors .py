# rock paper scissors

import random
userscore=0
computerscore=0

print("1.rock")
print("2.paper")
print("3.scissors")

while True:
    user_choice=int(input("enter your choice:"))
    computer_choice=random.randint(1,3)

    if (user_choice==1 and computer_choice==1):
        print("Computer chose:", computer_choice)
        print("match draw")
    elif (user_choice==1 and computer_choice==2):
        print("Computer chose:", computer_choice)
        print("you loose")
        computerscore=computerscore+1
    elif (user_choice==1 and computer_choice==3):
        print("Computer chose:", computer_choice)
        print("you win")
        userscore=score+1
    elif (user_choice==2 and computer_choice==1):
        print("Computer chose:", computer_choice)
        print("you won")
        userscore=score+1
    elif (user_choice==2 and computer_choice==2):
        print("Computer chose:", computer_choice)
        print("match draw")
    elif (user_choice==2 and computer_choice==3):
        print("Computer chose:", computer_choice)
        print("you lost")
        computerscore=computerscore+1
    elif (user_choice==3 and computer_choice==1):
        print("Computer chose:", computer_choice)
        print("you lost")
        computerscore=computerscore+1
    elif (user_choice==3 and computer_choice==2):
        print("Computer chose:", computer_choice)
        print("you won")
        userscore=score+1
    elif (user_choice==3 and computer_choice==3):
        print("Computer chose:", computer_choice)
        print("match draw")

    option=input("do you want to continue the game(yes or no):")

    if option.lower() != "yes":
        print("thanks for playing")
        break

print("your score is:",userscore,"and computer score is:",computerscore)
       
    
    
