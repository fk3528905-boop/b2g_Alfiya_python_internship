no = int(input("Enter no: "))

print(f"----Multiplication table of {no}----")

for i in range(1 , 11):
    result = no * i
    print(f"{no} X {i} = {result}")