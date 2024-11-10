import os


# File to store the ticket counter
TICKET_COUNTER_FILE = "ticket_counter.txt"

# Function to read the saved ticket number from the file
def load_ticket_counter():
    if os.path.exists(TICKET_COUNTER_FILE):
        with open(TICKET_COUNTER_FILE, 'r') as file:
            return int(file.read().strip())
    return 1  # Start from 1 if no file exists

# Function to save the current ticket counter to a file
def save_ticket_counter(ticket_counter):
    with open(TICKET_COUNTER_FILE, 'w') as file:
        file.write(str(ticket_counter))

# Initialize the ticket counter from the file
ticket_counter = load_ticket_counter()

# Function to generate sequential ticket numbers with a limit of 300
def generate_ticket_number():
    global ticket_counter

    # Check if the counter exceeds 300
    if ticket_counter >= 300:
        ticket_counter = 1  # Reset to 1 if it goes beyond 300

    # Get the current ticket number
    ticket_number = ticket_counter

    # Increment the counter for the next ticket
    ticket_counter += 1

    # Save the updated ticket counter to the file
    save_ticket_counter(ticket_counter)

    return ticket_number