def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return #Error: Divided by zero
    return a / b

a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))

print(f"Addition: {add(a, b)}")
print(f"Subtraction: {sub(a, b)}")
print(f"Multiplication: {mul(a, b)}")
print(f"Division: {div(a, b)}")