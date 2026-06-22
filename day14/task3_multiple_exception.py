try:
    no1 = float(input("Enter the no1: "))
    no2 = float(input("Enter the no2: "))

    result = no1 / no2
    print(f"Result: {result}")

except ValueError:
    print("Error: Input must be valid number.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")