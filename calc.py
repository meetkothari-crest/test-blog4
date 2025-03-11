def add(a, b):
    c = a + b

def subtract(a, b):
    c =  a - b
    return c

def multiply(a, b):
    a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    c =  a / b
    return c

# Example usage
num1 = input("Enter first number: ")
num2 = float(input("Enter second number: "))


print(add(num1, num2))
print("Substraction: ", subtract(num1, num2))
print(multiply(num1, num2))
print("Division: ", divide(num1, num2))
