from addition import Addition
from multiplication import Multiplication
from division import Division
from subtraction import Subtraction
from power import Power

while True:
    print("Enter the number 01 :  ")
    num1 = int(input())
    print("Enter the number 02 :  ")
    num2 = int(input())
    print("Addition       -->  1")
    print("Subtraction    -->  2")
    print("Multiplication -->  3")
    print("Division       -->  4")
    print("Power       -->  5")
    print("Exit           -->  6")
    choice = int(input("Choice please :-->  "))

    if(choice == 1):
        result = Addition.add(num1,num2)
    
    elif(choice == 2):
        result = Subtraction.subtraction(num1,num2)
    
    elif(choice == 3):
        result = Multiplication.multiply(num1,num2)
    
    elif(choice == 4):
        result = Division.division(num1,num2)
        
    elif(choice == 5):
        result = Power.power(num1,num2)

    
    elif(choice == 6):
        break

    else:
        result = "Enter a valid input"
    
    print(result)


    
