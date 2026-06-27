contacts = {}
while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Contact Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email ID: ")
        contacts[name] = {
            "Phone": phone,
            "Email": email
        }
        print("Contact added successfully.")
    elif choice == 2:
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in contacts.items():
                print("Name :", name)
                print("Phone:", details["Phone"])
                print("Email:", details["Email"])
                print("------------------------")
    elif choice == 3:
        name = input("Enter Contact Name to search: ")
        if name in contacts:
            print("Name :", name)
            print("Phone:", contacts[name]["Phone"])
            print("Email:", contacts[name]["Email"])
        else:
            print("Contact not found.")
    elif choice == 4:
        name = input("Enter Contact Name to update: ")
        if name in contacts:
            phone = input("Enter New Phone Number: ")
            email = input("Enter New Email ID: ")
            contacts[name]["Phone"] = phone
            contacts[name]["Email"] = email
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    elif choice == 5:
        name = input("Enter Contact Name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == 6:
        print("Thank you! Exiting Contact Management System.")
        break
    else:
        print("Invalid choice! Please try again.")