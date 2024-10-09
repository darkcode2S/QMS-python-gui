import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import random
import re
from db import create_connection

def visitor_queue(root, button_text, select_student, purpose):
    user_visitor = ctk.CTkToplevel(root)
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
    heading_label = ctk.CTkLabel(frame, text="Goood Day, Dear Visitor",
                                font=ctk.CTkFont(size=30, weight="bold"), 
                                text_color="#000000", anchor="center")
    heading_label.pack(pady=(20, 0), padx=(0,20))

    sub_label = ctk.CTkLabel(frame, text="Please enter your name and contact number.",
                                font=ctk.CTkFont(size=20, weight="bold"), 
                                text_color="#000000", anchor="center")
    sub_label.pack(pady=(20, 0), padx=(0,20))

    e1 = ctk.CTkEntry(frame, 
                    placeholder_text='Enter your name', 
                    width=420, 
                    height=70,
                    font=ctk.CTkFont(size=20, weight="bold"),
                    justify='center',
                    border_color='#d68b26'
                    )
    e1.pack(pady=20,padx=20)

    e2 = ctk.CTkEntry(frame, 
                    placeholder_text='Your contact number', 
                    width=300, 
                    height=70, 
                    font=ctk.CTkFont(size=20, weight="bold"),
                    justify='center',
                    border_color='#d68b26'
                    )
    e2.pack(pady=5,padx=20)

    mini_label = ctk.CTkLabel(frame, text="Thabk you for visiting NCMC. Our Staff will assist you if you have any concenrns.",
                                text_color="#000000", anchor="center")
    mini_label.pack(padx=(0,20))

    small_label = ctk.CTkLabel(frame, text="Proceed to create a ticket, and take a seat. We will serve you shortly.",
                                text_color="#000000", anchor="center")
    small_label.pack(padx=(0,20))

    button_frame = ctk.CTkFrame(frame, width=700, height=300, fg_color="transparent")
    button_frame.pack(expand=True, pady=20)

    cancel_button = ctk.CTkButton(button_frame , height=35, text='Cancel', fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', 
                                  command=lambda:cancel())
    cancel_button.pack(side="left", padx=20)

    create_button = ctk.CTkButton(button_frame , height=35, text='Create Ticket', fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', command=lambda: create_ticket(button_text, select_student))
    create_button.pack(side="left", padx=20)



    def cancel():
        user_visitor.destroy()

    global ticket_number
    # Generate a random ticket number between 1 and 200
    ticket_number = random.randint(1, 200) 

    def create_ticket(button_text, select_student):
        connection = create_connection()
        if connection is None:
            print("Failed to connect to the database.")
            return

        cursor = connection.cursor()    

        visitor_name = e1.get()
        visitor_phone = e2.get()

        if not visitor_phone or not visitor_phone:
            messagebox.showerror("Error", "All fields are required.")
            return
        
        phone_pattern = r'^\+?\d{10,15}$' 
        # Validate phone number format
        if not re.match(phone_pattern, visitor_phone):
            messagebox.showerror("Error", "Error: Invalid phone number format. Please enter a valid number with 10-15 digits.")
            return

         # Insert into queue table
        query_insert = """
                INSERT INTO `queue` (`queue_number`, `school_id`, `full_name`, `transaction`, `affiliation`, `phone`, `purpose_of_visit`) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
        # Use actual values instead of placeholders
        cursor.execute(query_insert, (
                ticket_number, 
                "None",              
                visitor_name,    
                button_text,    
                select_student,
                visitor_phone,
                purpose
            ))
                        
        # Commit the changes
        connection.commit()
        root.destroy()
        open_ticket_window(visitor_name)


        connection.close()       


    user_visitor.grab_set()

#Example print
def print_ticket(ticket_number, visitor_name):
    # Create a new window for printing the ticket
    print_window = tk.Tk()
    print_window.title("Print Ticket")

    # Create a label for the ticket
    ticket_label = tk.Label(print_window, text=f"Ticket Number: {ticket_number}\nStudent Name: {visitor_name}", font=("Helvetica", 16))
    ticket_label.pack(pady=10)

    # Add a button to close the print window
    close_button = tk.Button(print_window, text="Close", command=print_window.destroy)
    close_button.pack(pady=5)

    print_window.mainloop()

def open_ticket_window(visitor_name):
    new_window = tk.Tk()  # Create a new window
    new_window.title("Create Ticket")
    

    
    # Create a label to display the random ticket number
    label = tk.Label(new_window, text=f"Your Ticket Number: {ticket_number}", font=("Helvetica", 16))
    label.pack(pady=10)
    
    # Add a button to print the ticket
    print_button = tk.Button(new_window, text="Print Ticket", command=lambda: print_ticket(ticket_number, visitor_name))
    print_button.pack(pady=5)
    
    # Add a button to close the window
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=5)

    new_window.mainloop()


