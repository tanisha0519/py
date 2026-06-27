tickets = {}
while True:
    print("\n===== Ticket Booking System =====")
    print("1. Book Ticket")
    print("2. View Bookings")
    print("3. Search Booking")
    print("4. Cancel Ticket")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ticket_id = input("Enter Ticket ID: ")
        name = input("Enter Passenger Name: ")
        destination = input("Enter Destination: ")
        seats = int(input("Enter Number of Seats: "))
        tickets[ticket_id] = {
            "Name": name,
            "Destination": destination,
            "Seats": seats
        }
        print("Ticket booked successfully.")
    elif choice == 2:
        if len(tickets) == 0:
            print("No bookings found.")
        else:
            print("\nBooked Tickets:")
            for ticket_id, details in tickets.items():
                print("Ticket ID:", ticket_id)
                print("Passenger Name:", details["Name"])
                print("Destination:", details["Destination"])
                print("Seats:", details["Seats"])
                print("---------------------------")
    elif choice == 3:
        ticket_id = input("Enter Ticket ID to search: ")
        if ticket_id in tickets:
            print("Passenger Name:", tickets[ticket_id]["Name"])
            print("Destination:", tickets[ticket_id]["Destination"])
            print("Seats:", tickets[ticket_id]["Seats"])
        else:
            print("Ticket not found.")
    elif choice == 4:
        ticket_id = input("Enter Ticket ID to cancel: ")
        if ticket_id in tickets:
            del tickets[ticket_id]
            print("Ticket cancelled successfully.")
        else:
            print("Ticket not found.")
    elif choice == 5:
        print("Thank you! Exiting Ticket Booking System.")
        break
    else:
        print("Invalid choice! Please try again.")