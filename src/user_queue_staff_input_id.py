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
    
    

    def generate_ticket(button_text, select_student):
        entered_id = e1.get()

        if not entered_id:
            messagebox.showwarning("Input Error", "Please input school ID.")
            return  

        print(f"School ID: {entered_id}") 

        # Establish database connection
        connection = create_connection()
        if connection is None:
            print("Failed to connect to the database.")
            return

        try:
            cursor = connection.cursor()

            # Check if entered_id exists in the member table
            query_member = "SELECT school_id, full_name, affiliation, role, office FROM member WHERE school_id = %s"
            cursor.execute(query_member, (entered_id,))
            result_member = cursor.fetchone()

            if result_member:
                member_name = result_member[1]  

                # Generate ticket number only if a valid member is found
                from ticket import generate_ticket_number
                global ticket_number
                ticket_number = generate_ticket_number()


                import random

                cname = "Default"
                if button_text == "Cashier Service":
                    cname = random.choice(["C1", "C2"]) 

                    if cname == "C1":
                        
                        # Insert record into the queue table
                        query_insert = """
                                INSERT INTO `queue` (`queue_number`, `school_id`, `full_name`, `transaction`, `affiliation`, `purpose_of_visit`) 
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """
                        cursor.execute(query_insert, (
                            ticket_number,               
                            entered_id,
                            member_name,    
                            button_text,    
                            select_student,
                            purpose,
                        ))
                                            
                            # Commit the transaction and close the root window
                        connection.commit()
                        root.destroy()
                    else:
                        
                        # Insert record into the queue table
                        query_insert = """
                                INSERT INTO `queue_c2` (`queue_number`, `school_id`, `full_name`, `transaction`, `affiliation`, `purpose_of_visit`) 
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """
                        cursor.execute(query_insert, (
                            ticket_number,               
                            entered_id,
                            member_name,    
                            button_text,    
                            select_student,
                            purpose,
                        ))
                                            
                            # Commit the transaction and close the root window
                        connection.commit()
                        root.destroy()

                elif button_text == "Promisorry note coordinator":
                    cname = "PNC"

                    if cname == "PNC":
                        
                        # Insert record into the queue table
                        query_insert = """
                                INSERT INTO `queue` (`queue_number`, `school_id`, `full_name`, `transaction`, `affiliation`, `purpose_of_visit`) 
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """
                        cursor.execute(query_insert, (
                            ticket_number,               
                            entered_id,
                            member_name,    
                            button_text,    
                            select_student,
                            purpose,
                        ))
                                            
                            # Commit the transaction and close the root window
                        connection.commit()
                        root.destroy()

                elif button_text == "Scholarship coordinator":
                    cname = "SC"

                    if cname == "SC":
                                
                        # Insert record into the queue table
                        query_insert = """
                                INSERT INTO `queue` (`queue_number`, `school_id`, `full_name`, `transaction`, `affiliation`, `purpose_of_visit`) 
                                VALUES (%s, %s, %s, %s, %s, %s)
                            """
                        cursor.execute(query_insert, (
                            ticket_number,               
                            entered_id,
                            member_name,    
                            button_text,    
                            select_student,
                            purpose,
                        ))
                                            
                            # Commit the transaction and close the root window
                        connection.commit()
                        root.destroy()

                # Open ticket window
                open_ticket_window(ticket_number, cname)

                # Import and run example function from user_queue_entry_main
                from user_queue_entry_main import example
                example()

            else:
                # If not found in the member table, check in the student table
                query_student = "SELECT * FROM student WHERE school_id = %s"
                cursor.execute(query_student, (entered_id,))
                result_student = cursor.fetchone()

                if result_student:
                    print(f"School ID {entered_id} found in the student table.")
                    messagebox.showinfo("Student Access", f"The ID {entered_id} belongs to a Student.")
                else:
                    print(f"School ID {entered_id} not found in either table.")
                    messagebox.showinfo("Info", "You entered an invalid ID number. Please make sure you enter a valid ID number.")

        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Error during ticket generation: {e}")

        finally:
            # Close cursor and connection if they were opened
            if cursor:
                cursor.close()
            if connection:
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
        return True
    else:
        messagebox.showerror("Printer Error", "No printers found.")
        return False

# Function to print receipt
def print_receipt(ticket_number, cname, root):
    from datetime import datetime
    
    root.destroy() 

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





