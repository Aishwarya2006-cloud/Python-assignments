"""Create a Menu Driven application "CALC" by implemnting different functions for the following basic operations

a) Addition
b) Subtractio
Subtractio
c) Multiplication
d) Division
e) Modulus"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

while True:
    print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 6:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
    elif choice == 4:
        print("Result:", div(a, b))
    elif choice == 5:
        print("Result:", mod(a, b))
    else:
        print("Invalid choice")