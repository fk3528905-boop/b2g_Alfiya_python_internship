no = [11, 34, 56, 78, 45, 67]
print(f"Available Number: {no}")

target = int(input("Enter number to search: "))

print("-------serch the index value for element-------")
found = False
found_index = -1

for i in range(len(no)):
    if no[i] == target:
        found = True
        found_index = i
        break

if found:
    print(f"Found at index {found_index}!")
else:
    print("Not Found")
    