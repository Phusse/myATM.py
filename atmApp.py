import re

print("Welcome to Access Bank")

while True:
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if password == "1234":
        print(f"Hello {name}, welcome to Access Bank")
        accountBalance = float(1200000)
        print("A = Account balance")
        print("B = Withdrawal")
        print("C = Transfer")

        while True:
            option = input("Enter the option you want (A, B, C): ")

            if option == "A":
                print(f"Account balance: ${accountBalance}")

            elif option == "B":
                while True:
                    withdrawalAmount = input("How much do you want to withdraw? $")
                    if not re.match(r'^\d+(\.\d+)?$', withdrawalAmount):
                        print("Invalid withdrawal amount. Please enter a valid number.")
                    else:
                        withdrawalAmount = float(withdrawalAmount)
                        if withdrawalAmount > accountBalance:
                            print("Insufficient balance. Please fund your wallet.")
                        elif withdrawalAmount <= 0:
                            print("Invalid withdrawal amount. Please enter a positive number.")
                        else:
                            accountBalance -= withdrawalAmount
                            print(f"Withdrawal of ${withdrawalAmount} successful. Your new balance is ${accountBalance}")
                            break

            elif option == "C":
                print("A charge of $10 will be taken on each transfer.")
                while True:
                    transferAmount = input("How much would you like to transfer? $")
                    if not re.match(r'^\d+(\.\d+)?$', transferAmount):
                        print("Invalid transfer amount. Please enter a valid number.")
                    else:
                        transferAmount = float(transferAmount)
                        if transferAmount > accountBalance:
                            print("Insufficient balance. Please fund your account.")
                        elif transferAmount <= 0:
                            print("Invalid transfer amount. Please enter a positive number.")
                        else:
                            bank = input("Input bank: ")
                            accName = input("Account name: ")
                            while True:
                                accNum = input("Account Number: ")
                                if not re.match(r'^\d{10}$', accNum):
                                    print("Invalid account number. Please enter a 10-digit account number.")
                                else:
                                    break
                            accountBalance -= transferAmount + 10
                            print(f"Transfer of ${transferAmount} to {accName} was successful. Your new balance is ${accountBalance}")
                            break
            else:
                print("Please select a valid option")

            choice = input("Do you want to perform another operation? (y/n): ")
            if choice.lower() != "y":
                break
    else:
        print("Incorrect password. Please try again.")
