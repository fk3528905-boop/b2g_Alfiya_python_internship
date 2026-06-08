age = int(input("Enter your age:"))
has_id = input("do you valid id? (yes/no)").lower()

if age>18 and has_id == "yes":
    print("Elighbility")
else:
    print("not elighbility")
