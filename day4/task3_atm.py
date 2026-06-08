balance = 5000

print("Welcome to paython bank atm")
print("1.check balance")
print("2.Withdraw Amount")

choice = int(input("Enter your choice(1/2): "))

if choice == 1:
    print("your Balance: ",balance)

elif choice == 2:
    w_amount = float(input("Enter amount to withdraw: "))

    if w_amount <= balance:
        balance = balance - w_amount
        print("Transaction successful")
        print("Remaining Balance: ",int(balance))

    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")