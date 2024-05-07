#Task-1 Caculator
def calculator_function(num1,num2,choice):
    if choice == 1: 
        print("The Addition of The Values are :", num1+num2)
    elif choice == 2:
        print("The Subration of the Values are", num1-num2)
    elif choice == 3:
        print("The Mutiplication of the Values are : ", num1*num2)
    elif choice == 4:
        try :
            num3 = num1/num2
            print("The Division of the Values are : ",num3)
        except ZeroDivisionError as e:
           print(f"Occurs Error {e}")    
    elif choice == 5:
        try :
            num4= num1% num2
            print("The Modulus of the Values are : ",num4)
        except ZeroDivisionError as e:
           print(f"Occurs Error {e}") 
    elif choice == 6:
        print("The Exponent of the Values are : ",num1**num2)   
    else:
        print("Invalid input try again")

def menu():
    return "1.Add \n2.Subract \n3.Multiply \n4.Divide \n5.Modulus \n6.Exponent"   


while True:   
    print(menu())
    choice=int(input("Select One of The Following for Operation: "))
    if choice < 1 or choice > 6:
        print("Invalid Choice Selction!! Try Again..... ")
        continue
    a = float(input("Enter the 1st Value : "))
    b = float(input("Enter the 2nd Value : "))
    calculator_function(a,b,choice)       
    Tocontinue=input("Do you Want to continue (yes/no): ").lower()
    if(Tocontinue == "yes"):
        continue
    else:
         break
     