inventory = {}
while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pid = input("Enter Product ID: ")
        pname = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        inventory[pid] = {
            "Name": pname,
            "Quantity": quantity,
            "Price": price
        }
        print("Product added successfully.")
    elif choice == 2:
        if len(inventory) == 0:
            print("No products available.")
        else:
            print("\nProduct Details:")
            for pid, details in inventory.items():
                print("Product ID :", pid)
                print("Product Name :", details["Name"])
                print("Quantity :", details["Quantity"])
                print("Price :", details["Price"])
                print("---------------------------")
    elif choice == 3:
        pid = input("Enter Product ID to search: ")
        if pid in inventory:
            print("Product Name :", inventory[pid]["Name"])
            print("Quantity :", inventory[pid]["Quantity"])
            print("Price :", inventory[pid]["Price"])
        else:
            print("Product not found.")
    elif choice == 4:
        pid = input("Enter Product ID to update: ")
        if pid in inventory:
            quantity = int(input("Enter New Quantity: "))
            price = float(input("Enter New Price: "))
            inventory[pid]["Quantity"] = quantity
            inventory[pid]["Price"] = price
            print("Product updated successfully.")
        else:
            print("Product not found.")
    elif choice == 5:
        pid = input("Enter Product ID to delete: ")
        if pid in inventory:
            del inventory[pid]
            print("Product deleted successfully.")
        else:
            print("Product not found.")
    elif choice == 6:
        print("Thank you! Exiting Inventory Management System.")
        break
    else:
        print("Invalid choice! Please try again.")