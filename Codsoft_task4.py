#Task-4 Rock Paper Scissor
import random 
print("Welcome to the Game Rock,Paper and Scissor")
def computer_choice():
    randomchar="Rock","Paper","Scissor"
    computerchoice=random.choice(randomchar)
    print("The Computer Choice is :") 
    return computerchoice
def user_choice(userchoice,computerchoice):
    if(userchoice==computerchoice):
        return "Game Tie"
    elif(userchoice=="Paper" and computerchoice=="Rock") or (userchoice=="Scissor" and computerchoice=="Paper") or (userchoice=="Rock" and computerchoice=="Scissor"):
        return "User win the Game"
    else:
        return "User lose the Game"
while True:
    userchoice=input("Enter Your Choice(Rock or Paper or Scissor) : ")
    computerchoice=computer_choice()
    print(computerchoice)
    print(user_choice(userchoice,computerchoice))

    ToContinue=input("Do you want to Continue the Game(y/n):").lower()   
    if(ToContinue=="y"):
        continue
    else:
        break
       
             
    
