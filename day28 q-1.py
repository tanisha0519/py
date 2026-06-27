library = {}
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        library[book_id] = {
            "Book Name": book_name,
            "Author": author,
            "Status": "Available"
        }
        print("Book added successfully.")
    elif choice == 2:
        if len(library) == 0:
            print("No books available.")
        else:
            print("\nLibrary Books:")
            for book_id, details in library.items():
                print("Book ID :", book_id)
                print("Book Name :", details["Book Name"])
                print("Author :", details["Author"])
                print("Status :", details["Status"])
                print("---------------------------")
    elif choice == 3:
        book_id = input("Enter Book ID to search: ")
        if book_id in library:
            print("Book Name :", library[book_id]["Book Name"])
            print("Author :", library[book_id]["Author"])
            print("Status :", library[book_id]["Status"])
        else:
            print("Book not found.")
    elif choice == 4:
        book_id = input("Enter Book ID to issue: ")
        if book_id in library:
            if library[book_id]["Status"] == "Available":
                library[book_id]["Status"] = "Issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
        else:
            print("Book not found.")
    elif choice == 5:
        book_id = input("Enter Book ID to return: ")
        if book_id in library:
            if library[book_id]["Status"] == "Issued":
                library[book_id]["Status"] = "Available"
                print("Book returned successfully.")
            else:
                print("Book is already available.")
        else:
            print("Book not found.")
    elif choice == 6:
        book_id = input("Enter Book ID to delete: ")
        if book_id in library:
            del library[book_id]
            print("Book deleted successfully.")
        else:
            print("Book not found.")
    elif choice == 7:
        print("Thank you! Exiting Library Management System.")
        break
    else:
        print("Invalid choice! Please try again.")