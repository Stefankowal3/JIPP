def add(a, b):     
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

print("Please select the operation.")    
print("a. Add")    
print("b. Subtract")    
print("c. Multiply")    
print("d. Divide")   

op = input("Please enter choice (a/ b/ c/ d): ")   

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if op == 'a':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif op == 'b':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif op == 'c':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif op == 'd':
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid input! Please select a valid operation.")

