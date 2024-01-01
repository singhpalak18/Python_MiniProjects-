import math 
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "cannot divide by 0"
def square_root(x):
    if x>=0:
        return math.sqrt(x)
    else:
        return "invalid input for square root"
def power(x,y) :
    return x**y
def calculator():
    print("CALCULATOR")
    while True:
        print("Options ") 
        print("Enter 'add' for addition ")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply'for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'sqrt' for square root ")
        print("Enter 'power' for exponentiation")
        print("Enter 'quit' to end the program")
        user_input=input(":")
        if user_input=="quit":
            print("Exiting the calculator")
            break 
        if user_input in ["add","subtract","multiply","divide","sqrt","power"]:
            try:
                if user_input in["add","subtract","multiply","divide","power"]:
                    num1=float(input("Enter first number: "))
                    num2=float(input("Enter second number: "))
                else:
                    num1=float(input("Enter a number: "))
                if user_input=="add":
                    result= add(num1,num2)
                elif user_input=="subtract":
                    result=subtract(num1,num2)
                elif user_input=="multiply":
                    result=multiply(num1,num2)
                elif user_input=="divide":
                    result=divide(num1,num2)
                elif user_input == "sqrt":
                    result = square_root(num1)
                elif user_input == "power":
                    num3 = float(input("Enter the exponent: "))
                    result = power(num1, num3)

                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        else:
            print("Invalid input. Please enter a valid operation.")

if __name__ == "__main__":
    calculator()     
