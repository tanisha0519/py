while True:
    print("\n===== STRING OPERATION SYSTEM =====")
    print("1. Find Length")
    print("2. Reverse String")
    print("3. Convert to Uppercase")
    print("4. Convert to Lowercase")
    print("5. Check Palindrome")
    print("6. Count Vowels")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 7:
        print("Thank you! Exiting String Operation System.")
        break
    string = input("Enter a string: ")
    if choice == 1:
        print("Length of String =", len(string))
    elif choice == 2:
        print("Reversed String =", string[::-1])
    elif choice == 3:
        print("Uppercase String =", string.upper())
    elif choice == 4:
        print("Lowercase String =", string.lower())
    elif choice == 5:
        if string == string[::-1]:
            print("String is Palindrome.")
        else:
            print("String is Not Palindrome.")
    elif choice == 6:
        count = 0
        for ch in string.lower():
            if ch in "aeiou":
                count += 1
        print("Number of Vowels =", count)
    else:
        print("Invalid choice! Please try again.")