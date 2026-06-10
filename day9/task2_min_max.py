no = [10 , 12 , 24 ,37 , 11 , 90]
print(f"Array: {no}\n")

max = no[0]
min = no[0]

for num in no:
    if num > max:
        max = num
    if num < min:
        min = num

print("--------Min / Max----------")
print(f"Maximum= {max}")
print(f"Minimum= {min}")

