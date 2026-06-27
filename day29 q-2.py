arr = []
while True:
    print("\n===== ARRAY OPERATION SYSTEM =====")
    print("1. Insert Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Find Maximum Element")
    print("6. Find Minimum Element")
    print("7. Find Sum of Elements")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter element: "))
        arr.append(element)
        print("Element inserted successfully.")
    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Array Elements:", arr)
    elif choice == 3:
        key = int(input("Enter element to search: "))
        if key in arr:
            print("Element found at position", arr.index(key) + 1)
        else:
            print("Element not found.")
    elif choice == 4:
        key = int(input("Enter element to delete: "))
        if key in arr:
            arr.remove(key)
            print("Element deleted successfully.")
        else:
            print("Element not found.")
    elif choice == 5:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Maximum Element =", max(arr))
    elif choice == 6:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Minimum Element =", min(arr))
    elif choice == 7:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Sum of Elements =", sum(arr))
    elif choice == 8:
        print("Thank you! Exiting Array Operation System.")
        break
    else:
        print("Invalid choice! Please try again.")