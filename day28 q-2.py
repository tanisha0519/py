accounts = {}
while True:
    print("\n===== Bank Account System =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        acc_no = input("Enter Account Number: ")
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        accounts[acc_no] = {
            "Name": name,
            "Balance": balance
        }
        print("Account created successfully.")
    elif choice == 2:
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter Deposit Amount: "))
            accounts[acc_no]["Balance"] += amount
            print("Amount deposited successfully.")
        else:
            print("Account not found.")
    elif choice == 3:
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter Withdrawal Amount: "))
            if amount <= accounts[acc_no]["Balance"]:
                accounts[acc_no]["Balance"] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient Balance.")
        else:
            print("Account not found.")
    elif choice == 4:
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            print("Account Holder:", accounts[acc_no]["Name"])
            print("Available Balance:", accounts[acc_no]["Balance"])
        else:
            print("Account not found.")
    elif choice == 5:
        if len(accounts) == 0:
            print("No accounts available.")
        else:
            print("\nAccount Details:")
            for acc_no, details in accounts.items():
                print("Account Number:", acc_no)
                print("Account Holder:", details["Name"])
                print("Balance:", details["Balance"])
                print("--------------------------")
    elif choice == 6:
        print("Thank you! Exiting Bank Account System.")
        break
    else:
        print("Invalid choice! Please try again.")