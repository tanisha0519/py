balance=10000
while True:
    print("\n=====ATM MENU=====")
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4. exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("Available balance:",balance)
    elif choice==2:
        amount=int(input("enter deposit amount:"))
        balance+=amount
        print("amount deposited succesfully")
        print("updated balance:",balance)
    elif choice==3:
        amount=int(input("enter withdrawal amount:"))
        if amount<=balance:
            balance-=amount
            print("Please collect your cash")
            print("remaining balance:",balance)
        else:
            print("insufficient balance:")
    elif choice==4:
        print("tthank you for using ATM")
        break
    else:
        print("invalidchoice.please try again")





