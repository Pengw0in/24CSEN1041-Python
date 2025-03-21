accountBalance = 5000
with_ = int(input("Enter the amount to be withdrawn: "))
accountBalance -= with_

if with_ <= accountBalance:
    print(f"Withdrwal successful, remaining balance is {accountBalance} (╥_╥)")
else: 
    print("You suck, get a job (╯°□°)╯︵ ┻━┻ ")