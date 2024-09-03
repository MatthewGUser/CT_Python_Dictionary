# [ Task 1 ]

# Initialize with some sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

# Open a ticket
def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id in service_tickets:
        print("Error: Ticket ID already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"Ticket '{ticket_id}' opened successfully.")

# Update ticket
def update_ticket_status(ticket_id, new_status):
    if ticket_id not in service_tickets:
        print("Error: Ticket ID does not exist.")
    elif new_status not in ["open", "closed"]:
        print("Error: Invalid status. Use 'open' or 'closed'.")
    else:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket '{ticket_id}' status updated to '{new_status}'.")

# Display tickets
def display_tickets(filter_status=None):
    if filter_status:
        if filter_status not in ["open", "closed"]:
            print("Error: Invalid status filter. Use 'open' or 'closed'.")
            return
        filtered_tickets = {id: details for id, details in service_tickets.items() if details["Status"] == filter_status}
        if not filtered_tickets:
            print(f"No tickets with status '{filter_status}' found.")
        else:
            print(f"\nTickets with status '{filter_status}':")
            for id, details in filtered_tickets.items():
                print(f"ID: {id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
    else:
        print("\nAll Tickets:")
        for id, details in service_tickets.items():
            print(f"ID: {id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")

# Code hub
def main():
    # Loop through options until quit is selected
    while True:
        print("\nCustomer Service Ticket Tracker")
        print("1. Open a new ticket")
        print("2. Update ticket status")
        print("3. Display all tickets")
        print("4. Display tickets by status")
        print("5. Quit")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            ticket_id = input("Enter ticket ID: ").strip()
            customer_name = input("Enter customer name: ").strip()
            issue_description = input("Enter issue description: ").strip()
            open_ticket(ticket_id, customer_name, issue_description)
        elif choice == "2":
            ticket_id = input("Enter ticket ID: ").strip()
            new_status = input("Enter new status (open/closed): ").strip()
            update_ticket_status(ticket_id, new_status)
        elif choice == "3":
            display_tickets()
        elif choice == "4":
            status = input("Enter status to filter by (open/closed): ").strip()
            display_tickets(status)
        elif choice == "5":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Error: Invalid choice. Please select a number between 1 and 5.")

# Execute code
if __name__ == "__main__":
    main()
