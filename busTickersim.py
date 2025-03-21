def bus_ticket_booking():
    TOTAL_SEATS = 40
    TICKET_PRICE = 500
    available_seats = TOTAL_SEATS
    
    print("Welcome to the Bus Ticket Booking System!")
    print(f"Total available seats: {available_seats}")
    print(f"Ticket price: ₹{TICKET_PRICE} per ticket")
    
    while available_seats > 0:
    
        try:
            tickets_required = int(input("\nHow many tickets would you like to book? (Enter 0 to exit): "))

            if tickets_required == 0:
                print("Thank you for using the Bus Ticket Booking System!")
                break

            if tickets_required < 0:
                print("Please enter a valid number of tickets.")
                continue
                
            if tickets_required <= available_seats:
                total_cost = tickets_required * TICKET_PRICE
                available_seats -= tickets_required
                
                print(f"Booking successful! Total cost: ₹{total_cost}, Remaining seats: {available_seats}")
            else:
                print(f"Sorry, only {available_seats} seats available. Please reduce the number of tickets.")
        
        except ValueError:
            print("Please enter a valid number.")
    
    if available_seats == 0:
        print("\nAll seats have been booked!")


bus_ticket_booking()