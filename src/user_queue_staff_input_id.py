import customtkinter as ctk
import tkinter as tk
from PIL import Image
from db import create_connection
from tkinter import messagebox, simpledialog
import random

def satff_input_id(root, button_text, select_student, purpose):
    input_id_staff = tk.Toplevel(root)
    input_id_staff.title("Input ID Staff")
    input_id_staff.iconbitmap("old-logo.ico")

    # Set appearance mode and color theme (Light/Dark modes)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    # Center the window on the screen
    window_width = 800
    window_height = 600
    screen_width = input_id_staff.winfo_screenwidth()
    screen_height = input_id_staff.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    input_id_staff.geometry(f"{window_width}x{window_height}+{x}+{y}")

    main_frame = ctk.CTkFrame(input_id_staff, fg_color='transparent')
    main_frame.pack(expand=True)

    heading_label = ctk.CTkLabel(main_frame, text="PLEASE ENTER SCHOOL ID NUMBER",
                                        font=ctk.CTkFont(size=20, weight="bold"), 
                                        text_color="#000000", anchor="center")
    heading_label.pack(pady=(20,0), side='top')

    # Create the main frame for content
    frame = ctk.CTkFrame(main_frame, width=800, height=300, fg_color='#fff')
    frame.pack(expand=True, fill='both', padx=230)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)

    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)
    frame.rowconfigure(5, weight=1)

    e1 = ctk.CTkEntry(frame, height=60, font=ctk.CTkFont(size=20, weight="bold"), placeholder_text='0')
    e1.grid(row=0, column=0, columnspan=3, sticky='wnes', pady=5, padx=5)

        # Function to append button text to the entry field
    def append_to_entry(text):
        current_text = e1.get()  
        e1.delete(0, "end")  
        e1.insert("end", current_text + text)  

    # Function to delete the last character
    def delete_last_char():
        current_text = e1.get()
        e1.delete(0, "end")
        e1.insert("end", current_text[:-1]) 

    # Function to clear the entry field
    def clear_entry():
        e1.delete(0, "end")

    b1 = ctk.CTkButton(frame, text='1',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('1'))
    b1.grid(row=1, column=0, sticky='wnes', pady=5, padx=5)
    b2 = ctk.CTkButton(frame, text='2',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('2'))
    b2.grid(row=1, column=1, sticky='wnes', pady=5, padx=5)
    b3 = ctk.CTkButton(frame, text='3',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('3'))
    b3.grid(row=1, column=2, sticky='wnes', pady=5, padx=5)

    b4 = ctk.CTkButton(frame, text='4',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('4'))
    b4.grid(row=2, column=0, sticky='wnes', pady=5, padx=5)
    b5 = ctk.CTkButton(frame, text='5',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('5'))
    b5.grid(row=2, column=1, sticky='wnes', pady=5, padx=5)
    b6 = ctk.CTkButton(frame, text='6',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('6'))
    b6.grid(row=2, column=2, sticky='wnes', pady=5, padx=5)

    b7 = ctk.CTkButton(frame, text='7',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('7'))
    b7.grid(row=3, column=0, sticky='wnes', pady=5, padx=5)
    b8 = ctk.CTkButton(frame, text='8',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('8'))
    b8.grid(row=3, column=1, sticky='wnes', pady=5, padx=5)
    b9 = ctk.CTkButton(frame, text='9',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('9'))
    b9.grid(row=3, column=2, sticky='wnes', pady=5, padx=5)

    dash_button = ctk.CTkButton(frame, text='-', fg_color="#d68b26", hover_color="#a45e14", text_color='#fff', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('-'))
    dash_button.grid(row=4, column=2, sticky='wnes', pady=5, padx=5)

    delete_button = ctk.CTkButton(frame, text='Del', fg_color="#d68b26", hover_color="#a45e14", text_color='#fff', border_width=1, border_color='#000', height=60, command=lambda: delete_last_char())
    delete_button .grid(row=4, column=0, sticky='wnes', pady=5, padx=5)
    b0 = ctk.CTkButton(frame, text='0',fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', height=60, command=lambda: append_to_entry('0'))
    b0.grid(row=4, column=1, sticky='wnes', pady=5, padx=5)
    clear_button = ctk.CTkButton(frame, text='Clear', fg_color="#d68b26", hover_color="#a45e14", text_color='#fff', border_width=1, border_color='#000', height=60, command=lambda: clear_entry())
    clear_button.grid(row=5, column=0, columnspan=3, sticky='wnes', pady=5, padx=5)


    heading_label = ctk.CTkLabel(main_frame, text="Please proceed to create a ticket after entering your",
                                        text_color="#000000", anchor="center")
    heading_label.pack(padx=(0,20))

    heading_label = ctk.CTkLabel(main_frame, text="school ID number.",
                                        text_color="#000000", anchor="center")
    heading_label.pack(padx=(0,20))

    button_frame = ctk.CTkFrame(main_frame, fg_color='transparent')
    button_frame.pack(expand=True)

    cancel_button = ctk.CTkButton(button_frame, height=35, text='Cancel', fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000',command=lambda:cancel())
    cancel_button.pack(side='left', pady=20, padx=20)

    create_ticket = ctk.CTkButton(button_frame, height=35, text='Create Ticket', fg_color='#fff', hover_color="#a45e14", text_color='#000', border_width=1, border_color='#000', command=lambda: generate_ticket(button_text, select_student))
    create_ticket.pack(side='left', padx=20)

    def cancel():
        input_id_staff.destroy()
    
    global ticket_number
    # Generate a random ticket number between 1 and 200
    ticket_number = random.randint(1, 200) 
    
    def generate_ticket(button_text, select_student):
        entered_id = e1.get()

        if not entered_id:
            messagebox.showwarning("Input Error", "Please input school ID.")
            return  

        print(f"School ID: {entered_id}") 

        connection = create_connection()
        if connection is None:
            print("Failed to connect to the database.")
            return

        cursor = connection.cursor()

        # First, check in the student table
        query_student = "SELECT school_id, full_name, affiliation, role, office FROM member WHERE school_id = %s"
        cursor.execute(query_student, (entered_id,))
        result_member = cursor.fetchone()

        # Check if student exists
        if result_member:
            # Assuming result_member[1] is the full name
            member_name = result_member[1]  
            
            # Insert into queue table
            query_insert = """
                INSERT INTO `queue` (`queue_number`, `school_id`, `full_name`, `transaction`, `affiliation`, `purpose_of_visit`) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            # Use actual values instead of placeholders
            cursor.execute(query_insert, (
                ticket_number,               
                entered_id,
                member_name,    
                button_text,    
                select_student,
                purpose, 
            ))
                        
            # Commit the changes
            connection.commit()
            root.destroy()
            open_ticket_window(member_name)
            from user_queue_entry_main import example
            example()

        else:
            query_student = "SELECT * FROM student WHERE school_id = %s"
            cursor.execute(query_student, (entered_id,))
            result_student = cursor.fetchone()

            if result_student:
                print(f"School ID {entered_id} found in the member table.")
                messagebox.showinfo("Student Access", f"The ID {entered_id} belongs to Student.")
            else:
                print(f"School ID {entered_id} not found in either table.")
                messagebox.showinfo("Info", "You entered an invalid ID number. Please make sure you enter a valid ID number.")

        connection.close()

    input_id_staff.grab_set()

#Example print
def print_ticket(ticket_number, member_name):
    # Create a new window for printing the ticket
    print_window = tk.Tk()
    print_window.title("Print Ticket")

    # Create a label for the ticket
    ticket_label = tk.Label(print_window, text=f"Ticket Number: {ticket_number}\nStudent Name: {member_name}", font=("Helvetica", 16))
    ticket_label.pack(pady=10)

    # Add a button to close the print window
    close_button = tk.Button(print_window, text="Close", command=print_window.destroy)
    close_button.pack(pady=5)

    print_window.mainloop()

def open_ticket_window(member_name):
    new_window = tk.Tk()  # Create a new window
    new_window.title("Create Ticket")
    

    
    # Create a label to display the random ticket number
    label = tk.Label(new_window, text=f"Your Ticket Number: {ticket_number}", font=("Helvetica", 16))
    label.pack(pady=10)
    
    # Add a button to print the ticket
    print_button = tk.Button(new_window, text="Print Ticket", command=lambda: print_ticket(ticket_number, member_name))
    print_button.pack(pady=5)
    
    # Add a button to close the window
    close_button = tk.Button(new_window, text="Close", command=new_window.destroy)
    close_button.pack(pady=5)

    new_window.mainloop()




