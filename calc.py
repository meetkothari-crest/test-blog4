def add(a, b):
    c = a + b
    return c

def subtract(a, b):
    c = a - b 
    return c

def multiply(a, b):
    c = a * b
    return c  

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    c = a / b
    return c

# Example usage
num1 = float(input("Enter first number: "))  
num2 = float(input("Enter second number: "))


print("Addition: ", add(num1, num2))
print("Subtraction: ", subtract(num1, num2)) 
print("Multiplication: ", multiply(num1, num2))
print("Division: ", divide(num1, num2))