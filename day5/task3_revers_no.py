no = input("Enter the numner: ")

no_val = int(no)
rev_val = 0

while no_val > 0:
    last_digit = no_val % 10
    rev_val = (rev_val * 10) + last_digit
    no_val = no_val // 10

print("Reverse no is: ",rev_val)