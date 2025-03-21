accountBalance = 5000
while True:
    with_ = int(input("Enter the amount to be withdrawn: "))
    accountBalance -= with_
    if accountBalance <= 0:
        break

    if with_ <= accountBalance:
        print(f"Withdrwal successful, remaining balance: {accountBalance}")
    else: 
        print("Not enough Balance in account")