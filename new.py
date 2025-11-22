#Calculator functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

print("Calculator functions are ready to use.")
print("enter 1 for addition")
print("enter 2 for subtraction")
print("enter 3 for multiplication")
print("enter 4 for division")
print("enter 5 for power")
print("enter 6 for modulus")
choice = input("Select operation (1/2/3/4/5/6): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")

elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

elif choice == '4':
    try:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    except ValueError as e:
        print(e)

elif choice == '5':
    print(f"{num1} ^ {num2} = {power(num1, num2)}")

elif choice == '6':
    print(f"{num1} % {num2} = {modulus(num1, num2)}")