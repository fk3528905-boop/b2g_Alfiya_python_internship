print("Enter 3 student names: ")

with open("student.txt" , "w") as file:
    for i in range(1, 4):
        name = input(f"Student{i}: ")
        file.write(f"{name}\n")

print("\nSaved to students.txt Let's read it:")

with open("student.txt" , "r") as file:
    print(file.read())