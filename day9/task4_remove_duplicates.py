orig_list = [1 , 2, 2, 3, 4, 5, 6, 3, 1]
print(f"original lis/array: {orig_list}\n")

unique_list = []

for item in orig_list:
    if item not in unique_list:
        unique_list.append(item)

print("-----remove duplicate array/list------")
print(f"Clean List/array: {unique_list}") 