print("================================================================")
print(" PYTHON SMART CALCULATOR")
print("================================================================")

while True:
    print("\n----Menu-----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice:")
    if choice == '5':
        print("\nThank you for using Smart Calculator. Goodbye! ")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            no1 = float(input("Enter first number: "))
            no2 = float(input("Enter second number: "))
        except ValueError:
            print(" Invalid input! Please enter numbers only.")
            continue
      
    if choice == '1':
      print(f"Result: {no1} + {no2} = {no1 + no2}")

    elif choice == '2':
      print(f"Result: {no1} - {no2} = {no1 - no2}")

    elif choice == '3':
      print(f"Result: {no1} * {no2} = {no1 * no2}")

    elif choice == '4':
      # Handling division by zero
      if no2 == 0:
         print(" Error: Division by zero is not allowed!")
      else:
         print(f"Result: {no1} / {no2} = {no1 / no2}")
    else:
         print(" Invalid Choice!")