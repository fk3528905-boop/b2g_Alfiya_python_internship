def is_prime(no):
    if no <= 1:
        return False
    
    for i in range(2, no):
        if no % i == 0:
            return False
        
    return True

num = int(input("Enter the number: "))

if is_prime(num):
    print("Number is Prime")
else:
    print("Number is not Prime")