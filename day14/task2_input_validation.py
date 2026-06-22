try:
    age = int(input("Enter your age: "))
    print(f"you are {age} years old.")

except ValueError:
    print("Error: Please enter a valid numberical age.(e.g.20) not allow character.(e.g. xyz)")