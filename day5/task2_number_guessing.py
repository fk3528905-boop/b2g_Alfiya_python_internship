import random


s_no = random.randint(1 , 20)
print("welcome to number guessing game! I have picked a number betwwen 1 to 100. ")

while True:
    guess = int(input("Enter your guess: "))

    if guess > s_no:
        print("To high")
    
    elif guess < s_no:
        print("To Low")  
    
    else:
        print("correct")
    
    break