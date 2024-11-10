import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import re
from db import create_connection


def visitor_queue(root, button_text, select_student, purpose):
    user_visitor = tk.Toplevel(root)
    user_visitor.title("Visitor")
    user_visitor.iconbitmap("old-logo.ico")

    # Set appearance mode and color theme (Light/Dark modes)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    # Center the window on the screen
    window_width = 800
    window_height = 440
    screen_width = user_visitor.winfo_screenwidth()
    screen_height = user_visitor.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    user_visitor.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the main frame for content
    frame = ctk.CTkFrame(user_visitor, width=700, height=300, fg_color="transparent")
    frame.pack(expand=True)

    # Create a bold heading label under the image
    heading_label = ctk.CTkLabel(frame, text="Good Day, Dear Visitor",
                                font=ctk.CTkFont(size=30, weight="bold"), 
                                text_color="#000000", anchor="center")
    heading_label.pack(pady=(20, 0), padx=(0, 20))

    sub_label = ctk.CTkLabel(frame, text="Please enter your name and contact number.",
                                font=ctk.CTkFont(size=20, weight="bold"), 
                                text_color="#000000", anchor="center")
    sub_label.pack(pady=(20, 0), padx=(0, 20))

    e1 = ctk.CTkEntry(frame, 
                    placeholder_text='Enter your name', 
                    width=420, 
                    height=70,
                    font=ctk.CTkFont(size=20, weight="bold"),
                    justify='center',
                    border_color='#d68b26'
                    )
    e1.pack(pady=20, padx=20)

    e2 = ctk.CTkEntry(frame, 
                    placeholder_text='Your contact number', 
                    width=300, 
                    height=70, 
                    font=ctk.CTkFont(size=20, weight="bold"),
                    justify='center',
                    border_color='#d68b26'
                    )
    e2.pack(pady=5, padx=20)

    mini_label = ctk.CTkLabel(frame, text="Thank you for visiting NCMC. Our Staff will assist you if you have any concerns.",
                                text_color="#000000", anchor="center")
    mini_label.pack(padx=(0, 20))

    small_label = ctk.CTkLabel(frame, text="Proceed to create a ticket, and take a seat. We will serve you shortly.",
                                text_color="#000000", anchor="center")
    small_label.pack(padx=(0, 20))

    button_frame = ctk.CTkFrame(frame, width=700, height=300, fg_color="transparent")
    button_frame.pack(expand=True, pady=20)

    cancel_button = ctk.CTkButton(button_frame, height=35, text='Cancel', fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', 
                                  command=lambda: cancel())
    cancel_button.pack(side="left", padx=20)

    create_button = ctk.CTkButton(button_frame, height=35, text='Create Ticket', fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', 
                                  command=lambda: create_ticket(button_text, select_student, purpose))
    create_button.pack(side="left", padx=20)

    def cancel():
        user_visitor.destroy()


    def create_ticket(button_text, select_student, purpose):
        connection = create_connection()
        if connection is None:
            print("Failed to connect to the database.")
            return

        visitor_name = e1.get()
        visitor_phone = e2.get()

        # Validate that both fields are filled in
        if not visitor_name or not visitor_phone:
            messagebox.showerror("Error", "All fields are required.")
            return

        # Validate phone number format
        phone_pattern = r'^\+?\d{10,15}$' 
        if not re.match(phone_pattern, visitor_phone):
            messagebox.showerror("Error", "Invalid phone number format. Please enter a valid number with 10-15 digits.")
            return

        try:
            # Generate a unique ticket number
            global ticket_number
            from ticket import generate_ticket_number
            ticket_number = generate_ticket_number()
            
            cursor = connection.cursor()

            # Insert data into the queue table
            query_insert = """
                INSERT INTO `queue` (`queue_number`, `full_name`, `transaction`, `affiliation`, `phone`, `purpose_of_visit`) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(query_insert, (
                ticket_number,             
                visitor_name,    
                button_text,    
                select_student,
                visitor_phone,
                purpose
            ))

            # Commit the transaction to save changes
            connection.commit()

            # Close the user_visitor window
            root.destroy()

            # Determine the coordinator name code based on the button_text
            cname = "Default"
            if button_text == "Cashier Service":
                cname = "C1"
            elif button_text == "Promisorry note coordinator":
                cname = "PNC"
            elif button_text == "Scholarship coordinator":
                cname = "SC"

            # Open the ticket window with generated ticket information
            open_ticket_window(ticket_number, cname)

            # Import and run example function from user_queue_entry_main
            from user_queue_entry_main import example
            example()

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Database error: {e}")

        finally:
            # Close cursor and connection if they were opened
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    user_visitor.grab_set()

# Example print
def print_ticket(ticket_number, visitor_name):
    # Create a new window for printing the ticket
    print_window = tk.Tk()
    print_window.title("Print Ticket")

    # Create a label for the ticket
    ticket_label = tk.Label(print_window, text=f"Ticket Number: {ticket_number}\nVisitor Name: {visitor_name}", font=("Helvetica", 16))
    ticket_label.pack(pady=10)

    # Add a button to close the print window
    close_button = tk.Button(print_window, text="Close", command=print_window.destroy)
    close_button.pack(pady=5)

    print_window.mainloop()

def open_ticket_window( ticket_number, cname):
    import tkinter as tk
    from tkinter import font
    from datetime import datetime

    from center_window import center_window


        # Initialize the main window
    root = tk.Tk()
    root.title("View Queue Ticket")
    center_window(800, 600, root)
    root.configure(bg="#D3D3D3")  # Light gray background for the window

    root.iconbitmap("old-logo.ico")

        # Custom font for larger text
    large_font = font.Font(family="Helvetica", size=48, weight="bold")
    title_font = font.Font(family="Helvetica", size=30, weight="bold")
    medium_font = font.Font(family="Helvetica", size=15)
    small_font = font.Font(family="Helvetica", size=10)

    # Title Label
    title_label = tk.Label(root, text="VIEW QUEUE TICKET", font=title_font, bg="#D3D3D3")
    title_label.pack(pady=10)

        # Frame for ticket information
    ticket_frame = tk.Frame(root, bg="white", padx=20, pady=20)
    ticket_frame.pack(pady=10)

        # Get current date in MM-DD-YY format
    current_date = datetime.now().strftime("%m-%d-%y")

        # Ticket Number
    queue_number_label = tk.Label(ticket_frame, text="YOUR QUEUE NUMBER:", font=small_font, fg="black", bg="white")
    queue_number_label.pack()

    queue_label = tk.Label(ticket_frame, text=ticket_number, font=large_font, fg="black", bg="white")
    queue_label.pack()

    window_label = tk.Label(ticket_frame, text="WINDOW:", font=small_font, fg="black", bg="white")
    window_label.pack()

        # Counter Information
    counter_label = tk.Label(ticket_frame, text=cname, font=large_font, fg="black", bg="white")
    counter_label.pack()

    seated_label = tk.Label(ticket_frame, text="PLEASE BE SEATED.\n YOU WILL BE SERVED SHORTLY.", font=small_font, fg="black", bg="white")
    seated_label.pack()

    queue_label = tk.Label(ticket_frame, text=current_date, font=small_font, fg="black", bg="white")
    queue_label.pack(pady=(20,10), anchor="e")

        # Instructional Text
    instruction_label = tk.Label(root, text=f" Click Print Ticket to generate your queue ticket.\n"
                                                "Thank you for your submission! We appreciate your feedback. if you have any\n further inquiries or concerns, please don't hesitate to reach out to us.",
                                    font=small_font, bg="#D3D3D3")
    instruction_label.pack(pady=10)

        # Next Ticket Button
    next_button = tk.Button(root, text="Print Ticket", font=medium_font, command=lambda: print_receipt(ticket_number, cname, root))
    next_button.pack(pady=10)

        # Run the Tkinter event loop
    root.mainloop()

from zebra import Zebra

z = Zebra()

# Function to connect to the printer
def connect_printer():
    printers = z.getqueues()
    if printers:
        z.setqueue(printers[0])  # Automatically select the first printer
    else:
        print("No printers found.")
        return False
    return True

# Function to print receipt
def print_receipt(ticket_number, cname, root):
    from datetime import datetime

    root.destroy();

    if connect_printer():
        # ZPL code for formatting receipt to match the provided style
        zpl = f"""

------------------
YOUR QUEUE NUMBER
       {ticket_number}
        
      WINDOW
       {cname}
------------------
PLEASE BE SEATED.\nYOU WILL BE SERVED SHORTLY.

                 {datetime.now().strftime("%m-%d-%y")}


        """
        z.output(zpl)
        
        print("Receipt printed successfully!")
    else:
        print("Could not print receipt.")

