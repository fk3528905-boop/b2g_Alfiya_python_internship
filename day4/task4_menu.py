print("simple Menu")
print("1. addition")
print("2. subtraction")

choice = int(input("Enter your choice (1/2): "))

no1 = int(input("Enter no1: "))
no2 = int(input("Enter no2: "))

if choice == 1:
    result = no1 + no2
    print("Result: ",result)

elif choice == 2:
    result = no1 - no2
    print("Result: ",result)

else:
    print("Invalid choice")