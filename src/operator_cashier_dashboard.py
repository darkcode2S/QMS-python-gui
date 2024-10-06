import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from counter_staff_profile_interface import counter_staff_home
from db import create_connection

def cashier_window(op_name, op_area):
    counter_staff = ctk.CTk()
    counter_staff.title("Operator")
    counter_staff.iconbitmap("old-logo.ico")

    # Set appearance mode and color theme (Light/Dark modes)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    # Center the window on the screen
    window_width = 1000
    window_height = 600
    screen_width = counter_staff.winfo_screenwidth()
    screen_height = counter_staff.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    counter_staff.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the main frame for navigation-------------------------------------------------------------------------------------------------------------
    nav_frame = ctk.CTkFrame(counter_staff, width=700, height=60, fg_color='#d68b26')
    nav_frame.pack(side='top', fill='x', pady=10, padx=10)

    nav_button = ctk.CTkButton(nav_frame, 
                               text='Home', 
                               width=80, 
                               fg_color='#fff', 
                               text_color='#000',
                               hover_color='lightgray', 
                               command=lambda: back_home(op_name, op_area))
    nav_button.pack(side='left', pady=20, padx=20)

    #home button
    def back_home(op_name, op_area):
        counter_staff.destroy()
        counter_staff_home(op_name, op_area)
  
    title_label = ctk.CTkLabel(nav_frame,
                                text='Cashier window 1',
                                anchor='w',
                                compound='left', 
                                text_color='#fff',
                                font=ctk.CTkFont(size=15, weight="bold"))
    title_label.pack(side='left',pady=20)


    prep_num = ctk.CTkLabel(nav_frame,
                                text='07',
                                anchor='w',
                                compound='left', 
                                text_color='#000',
                                font=ctk.CTkFont(size=30, weight="bold"))
    prep_num.pack(side='right', pady=20, padx=(0,20))


    prep_label = ctk.CTkLabel(nav_frame,
                                text='Serving: ',
                                anchor='w',
                                compound='left', 
                                text_color='#fff',
                                font=ctk.CTkFont(size=15, weight="bold"))
    prep_label.pack(side='right', pady=20, padx=(20,0))

    serve_num = ctk.CTkLabel(nav_frame,
                                text='08',
                                anchor='w',
                                compound='left', 
                                text_color='#000',
                                font=ctk.CTkFont(size=30, weight="bold"))
    serve_num.pack(side='right',pady=20)

    serve_label = ctk.CTkLabel(nav_frame,
                                text='Preparing: ',
                                anchor='w',
                                compound='left', 
                                text_color='#fff',
                                font=ctk.CTkFont(size=15, weight="bold"))
    serve_label.pack(side='right',pady=20)



    # Create the table frame----------------------------------------------------------------------------------------------------------------------
    table_frame = ctk.CTkFrame(counter_staff, width=700, height=600, fg_color='transparent')
    table_frame.pack(side='bottom', fill='x', pady=10, padx=10)

    table_frame.columnconfigure(0, weight=1)
    table_frame.columnconfigure(1, weight=1)
    table_frame.rowconfigure(0, weight=1)


    def fetch_queue_data():
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT  queue_number, purpose_of_visit, affiliation FROM queue")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows

    # Define columns for the Treeview
    columns = ("Queue number", "Purpose of visit", "Affiliation")  # Ensure correct names

    # Create the first Treeview with a specified height
    tb1 = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)  # Set height to show 15 rows
    tb1.grid(row=0, column=0, padx=(0,10), sticky='news')

    # Configure column properties for tb1
    tb1.column("#0", width=0, stretch="no")
    tb1.column("Queue number", anchor="center", width=100)  # Increased width for better visibility
    tb1.column("Purpose of visit", anchor="center", width=200)  # Increased width for better visibility
    tb1.column("Affiliation", anchor="center", width=100)  # Increased width for better visibility

    # Configure headings for tb1
    tb1.heading("#0", text="")
    tb1.heading("Queue number", text="Queue Number") 
    tb1.heading("Purpose of visit", text="Purpose of Visit") 
    tb1.heading("Affiliation", text="Affiliation")

    # Fetch and display data
    data = fetch_queue_data()
    for row in data:
        tb1.insert("", "end", values=row)

    item_values = None

    #get value wehn selected operator table
    def on_item_selected_password(event):
        global item_values
        selected_item = tb1.selection()  # Get the selected items (returns a tuple)

        if selected_item:  # Check if any item is selected
            item_values = tb1.item(selected_item[0], 'values')  # Get the values of the selected item
            print(f"Selected values: {item_values}")  # Do something with the values
        else:
            print("No item selected")  # Handle the case where no item is selected

    tb1.bind("<<TreeviewSelect>>", on_item_selected_password)

    # Create the second Treeview with a specified height
    tb2 = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)  # Set height to show 15 rows
    tb2.grid(row=0, column=1, sticky='news')

    # Configure column properties for tb2
    tb2.column("#0", width=0, stretch="no")
    tb2.column("Queue number", anchor="center", width=100)  # Increased width for better visibility
    tb2.column("Purpose of visit", anchor="center", width=200)  # Increased width for better visibility
    tb2.column("Affiliation", anchor="center", width=100)  # Increased width for better visibility

    # Configure headings for tb2
    tb2.heading("#0", text="")
    tb2.heading("Queue number", text="Queue Number") 
    tb2.heading("Purpose of visit", text="Purpose of Visit") 
    tb2.heading("Affiliation", text="Affiliation")

    #table title name---------------------------------------------------------------------------------------------------------------------------
    table_name = ctk.CTkFrame(counter_staff, width=700, height=0, border_color='darkgray', border_width=1)
    table_name.pack(side='bottom', fill='x')

    table_name.columnconfigure(0, weight=1)
    table_name.columnconfigure(1, weight=1)
    table_name.rowconfigure(0, weight=1)

    heading_tit = ctk.CTkLabel(table_name,
                                text='Preparing list',
                                anchor='w',
                                compound='left', 
                                text_color='#000',
                                font=ctk.CTkFont(size=15, weight="bold"))
    heading_tit.grid(row=0, column=0, pady=3)

    heading_tit2 = ctk.CTkLabel(table_name,
                                text='Serving list',
                                anchor='w',
                                compound='left', 
                                text_color='#000',
                                font=ctk.CTkFont(size=15, weight="bold"))
    heading_tit2.grid(row=0, column=1, pady=3)

    #table button functions------------------------------------------------------------------------------------------------------------------------
    table_btn = ctk.CTkFrame(counter_staff, width=700, height=0, fg_color='transparent')
    table_btn.pack(side='bottom', fill='x', pady=10)

    table_btn.columnconfigure(0, weight=1)
    table_btn.columnconfigure(1, weight=1)
    table_btn.columnconfigure(2, weight=1)
    table_btn.columnconfigure(3, weight=1)
    table_btn.rowconfigure(0, weight=1)

    #button function interact database
    # Button function interacting with the database
    next_btn = ctk.CTkButton(
        table_btn, text='Next ticket',
        height=35, text_color='#fff'
    )
    next_btn.grid(row=0, column=0)

    call_btn = ctk.CTkButton(
        table_btn, text='Call ticket',
        height=35, text_color='#fff'
    )
    call_btn.grid(row=0, column=1)

    complete_btn = ctk.CTkButton(
        table_btn, text='Complete ticket',
        height=35, text_color='#fff'
    )
    complete_btn.grid(row=0, column=2)

    voided_btn = ctk.CTkButton(
        table_btn, text='Voided',
        height=35, text_color='#fff'
    )
    voided_btn.grid(row=0, column=3)


    # # Function to change the button text color on hover
    # def change_btn_text_color(button, hover_text_color):
    #     def on_enter(event):
    #         button.configure(text_color=hover_text_color)

    #     def on_leave(event):
    #         button.configure(text_color='#000')  # Set text back to black

    #     button.bind("<Enter>", on_enter)
    #     button.bind("<Leave>", on_leave)


    # # Applying hover effect on all buttons
    # change_btn_text_color(next_btn, '#fff')    # Set to white text on hover
    # change_btn_text_color(call_btn, '#fff')
    # change_btn_text_color(complete_btn, '#fff')
    # change_btn_text_color(voided_btn, '#fff')



    # Run the application
    counter_staff.mainloop()
