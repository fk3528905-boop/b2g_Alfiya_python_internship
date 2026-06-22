while True:
    try:
        age = int(input("Enter your age: "))
        break
    
    except ValueError:
        print("Invalid input. Please enter the  numbers only.")

print(f"Thank you. Your age is {age}.")