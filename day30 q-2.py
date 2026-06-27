books = []
while True:
    print("\n===== MINI LIBRARY SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book = input("Enter Book Name: ")
        books.append(book)
        print("Book added successfully.")
    elif choice == 2:
        if len(books) == 0:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])
    elif choice == 3:
        book = input("Enter Book Name to search: ")
        if book in books:
            print("Book is available in the library.")
        else:
            print("Book not found.")
    elif choice == 4:
        book = input("Enter Book Name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found.")
    elif choice == 5:
        print("Thank you! Exiting Mini Library System.")
        break
    else:
        print("Invalid choice! Please try again.")