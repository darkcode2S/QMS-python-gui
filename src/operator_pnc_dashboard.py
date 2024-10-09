import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from counter_staff_profile_interface import counter_staff_home
from db import create_connection
from tkinter import ttk, messagebox  # Added messagebox for displaying warnings


def pnc_window(op_name, op_area):
    promisorry = ctk.CTk()
    promisorry.title("Promisorry note")
    promisorry.iconbitmap("old-logo.ico")
    # Set appearance mode and color theme (Light/Dark modes)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    # Center the window on the screen
    window_width = 1000
    window_height = 600
    screen_width = promisorry.winfo_screenwidth()
    screen_height = promisorry.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    promisorry.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the main frame for navigation
    nav_frame = ctk.CTkFrame(promisorry, width=700, height=60, fg_color='#d68b26')
    nav_frame.pack(side='top', fill='x', pady=10, padx=10)

    nav_button = ctk.CTkButton(nav_frame, 
                               text='Home', 
                               width=80, 
                               fg_color='#fff', 
                               text_color='#000',
                               hover_color='lightgray', 
                               command=lambda: back_home(op_name, op_area))
    nav_button.pack(side='left', pady=20, padx=20)

    def back_home(op_name, op_area):
        promisorry.destroy()
        counter_staff_home(op_name, op_area)

    title_label = ctk.CTkLabel(nav_frame,
                                text='Cashier 1',
                                anchor='w',
                                compound='left', 
                                text_color='#fff',
                                font=ctk.CTkFont(size=30, weight="bold"))
    title_label.pack(side='left', pady=20)

    prep_num = ctk.CTkLabel(nav_frame,
                            text='00',
                            anchor='w',
                            compound='left', 
                            text_color='#fff',
                            font=ctk.CTkFont(size=50, weight="bold", family='Helvetica'))
    prep_num.pack(side='right', pady=20, padx=(0, 20))

    prep_label = ctk.CTkLabel(nav_frame,
                              text='Serving: ',
                              anchor='w',
                              compound='left', 
                              text_color='#fff',
                              font=ctk.CTkFont(size=30, weight="bold"))
    prep_label.pack(side='right', pady=20, padx=(20, 0))

    serve_num = ctk.CTkLabel(nav_frame,
                             text='00',
                             anchor='w',
                             compound='left', 
                             text_color='#fff',
                             font=ctk.CTkFont(size=50, weight="bold", family='Helvetica'))
    serve_num.pack(side='right', pady=20)

    serve_label = ctk.CTkLabel(nav_frame,
                               text='Preparing: ',
                               anchor='w',
                               compound='left', 
                               text_color='#fff',
                               font=ctk.CTkFont(size=30, weight="bold"))
    serve_label.pack(side='right', pady=20)

    # Create the table frame----------------------------------------------------------------------------------
    table_frame = ctk.CTkFrame(promisorry, width=700, height=800, fg_color='transparent')
    table_frame.pack(side='bottom', expand=True, fill='both', pady=10, padx=10)

    table_frame.columnconfigure(0, weight=1)
    table_frame.columnconfigure(1, weight=1)
    table_frame.rowconfigure(0, weight=1)

    def fetch_queue_data():
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT queue_number, purpose_of_visit, affiliation FROM queue WHERE transaction = 'Promisorry note coordinator'")
        rows = cursor.fetchall()
        cursor.close()
        connection.close()
        return rows

    columns = ("Queue number", "Purpose of visit", "Affiliation")

    # First Treeview (tb1)
    tb1 = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
    tb1.grid(row=0, column=0, padx=(0,10), sticky='news')
    tb1.column("#0", width=0, stretch="no")
    tb1.column("Queue number", anchor="center", width=100)
    tb1.column("Purpose of visit", anchor="center", width=200)
    tb1.column("Affiliation", anchor="center", width=100)
    tb1.heading("#0", text="")
    tb1.heading("Queue number", text="Queue Number")
    tb1.heading("Purpose of visit", text="Purpose of Visit")
    tb1.heading("Affiliation", text="Affiliation")

    data = fetch_queue_data()
    for row in data:
        tb1.insert("", "end", values=row)

    # Second Treeview (tb2)--------------------------------------------------------------------------------
    # Define a function to handle the selection event in tb2
    def on_tb2_select(event):
        # Get the selected item from tb2
        selected_item = tb2.selection()

        # Ensure that an item is selected
        if selected_item:
            # Retrieve the values of the selected item
            item_values = tb2.item(selected_item, 'values')

            # Create a small custom pop-up window
            popup = tk.Toplevel(promisorry)
            popup.geometry("350x150")  # Set the size of the pop-up window
            popup.title("Ticket Action")
            popup.resizable(False, False)

            # Display the selected values in the pop-up window (for reference)
            tk.Label(popup, text=f"Queue Number: {item_values[0]}", font=("Arial", 12)).pack(pady=10)
            tk.Label(popup, text=f"Purpose of Visit: {item_values[1]}", font=("Arial", 10)).pack()
            tk.Label(popup, text=f"Affiliation: {item_values[2]}", font=("Arial", 10)).pack()

            # Frame to hold the buttons
            button_frame = tk.Frame(popup)
            button_frame.pack(pady=20)

            # Function to handle the "Complete Ticket" button
            def complete_ticket():
                conn = create_connection()
                cursor = conn.cursor()
                
                # Perform any action needed (e.g., update database or UI)
                tk.messagebox.showinfo("Ticket Completed", f"Ticket {item_values[0]} has been marked as complete.")
                tb2.delete(selected_item)  # Remove the ticket from tb2
                popup.destroy()  # Close the pop-up window

                q_num = item_values[0]

                query = "DELETE FROM queue_display_promisorry"
                cursor.execute(query)
                conn.commit()

                query2 = "DELETE FROM queue WHERE queue_number = %s"
                cursor.execute(query2, (q_num,))
                conn.commit()

            # Function to handle the "Void Ticket" button
            def void_ticket():
                # Perform any action needed (e.g., update database or UI)
                tk.messagebox.showinfo("Ticket Voided", f"Ticket {item_values[0]} has been voided.")
                tb2.delete(selected_item)  # Remove the ticket from tb2
                popup.destroy()  # Close the pop-up window

            # Create buttons for completing or voiding the ticket
            complete_button = tk.Button(button_frame, text="Complete Ticket", width=15, bg="green", fg="white", command=complete_ticket)
            complete_button.pack(side="left", padx=10)

            void_button = tk.Button(button_frame, text="Void Ticket", width=15, bg="red", fg="white", command=void_ticket)
            void_button.pack(side="right", padx=10)
                

    # Create tb2 with columns and headers
    tb2 = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
    tb2.grid(row=0, column=1, sticky='news')
    tb2.column("#0", width=0, stretch="no")
    tb2.column("Queue number", anchor="center", width=100)
    tb2.column("Purpose of visit", anchor="center", width=200)
    tb2.column("Affiliation", anchor="center", width=100)
    tb2.heading("#0", text="")
    tb2.heading("Queue number", text="Queue Number")
    tb2.heading("Purpose of visit", text="Purpose of Visit")
    tb2.heading("Affiliation", text="Affiliation")

    # Bind the TreeviewSelect event to the on_tb2_select function
    tb2.bind("<<TreeviewSelect>>", on_tb2_select)
    #table title name---------------------------------------------------------------------------------------------------------------------------
    table_name = ctk.CTkFrame(promisorry, width=700, height=0, border_color='darkgray', border_width=1)
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
                                text='Serving',
                                anchor='w',
                                compound='left', 
                                text_color='#000',
                                font=ctk.CTkFont(size=15, weight="bold"))
    heading_tit2.grid(row=0, column=1, pady=3)


    # Selected item storage
    selected_item = None


    # Function to transfer selected item from tb1 to tb2
    def call_ticket():
        conn = create_connection()
        if conn is None:
            print("Failed to connect to the database.")
            return

        cursor = conn.cursor()

        # Check if tb2 already has data (a ticket is being processed)
        if tb2.get_children():
            # If tb2 has data, show a message and prevent further action
            messagebox.showwarning("Processing", "Please complete the current ticket before calling the next one.")
            return  # Exit the function if tb2 has data

        # Get all the children (items) in Treeview TB1
        children = tb1.get_children()

        # Check if tb1 is empty (no tickets available to process)
        if not children:
            # If tb1 is empty, show a message and prevent further action
            messagebox.showinfo("No Data", "No tickets found in the queue to process.")
            # Clear the "Serving" and "Preparing" labels
            prep_num.configure(text="--")
            serve_num.configure(text="--")
            return  # Exit the function early if tb1 has no data

        # Get the first item (the one that is being served)
        first_item = children[0]
        first_item_values = tb1.item(first_item, 'values')

        # Update the "Serving" label with the queue number of the first item
        prep_num.configure(text=first_item_values[0])

        q_num = first_item_values[0]

        print(q_num)

        query = "INSERT INTO queue_display_promisorry (promisorry_number) VALUES (%s)"
        cursor.execute(query, (q_num,))
        conn.commit()  # Commit the changes to the database

        cursor.close()
        conn.close()

        # Check if there's a second item to set for "Preparing"
        if len(children) > 1:
            second_item = children[1]
            second_item_values = tb1.item(second_item, 'values')
            # Update the "Preparing" label with the queue number of the second item
            serve_num.configure(text=second_item_values[0])

            s_num = second_item_values[0]
            print(s_num)

            conn = create_connection()
            if conn is None:
                print("Failed to connect to the database.")
                return

            cursor = conn.cursor()

            query = "INSERT INTO queue_display_promisorry (promisorry_number) VALUES (%s)"
            cursor.execute(query, (s_num,))
            conn.commit()  # Commit the changes to the database

            cursor.close()
            conn.close()
        else:
            # If there's no second item, clear the "Preparing" label
            serve_num.configure(text="--")

        # Automatically transfer the first item from tb1 to tb2
        tb2.insert("", 0, values=first_item_values)
        tb1.delete(first_item)  



    # Function to complete or void ticket in tb2
    def complete_or_void_ticket():
        if tb2.selection():
            tb2.delete(tb2.selection())  # Remove from tb2

    # Capture selected item from tb1
    def on_item_selected(event):
        global selected_item
        selected = tb1.selection()
        first_item = tb1.get_children()[0]  # Get the first item

        if selected:
            # # Check if the selected item is the first item in TB1
            # if selected[0] != first_item:
            #     # Show a warning message if the user clicks on any item other than the first one
            #     messagebox.showwarning("Invalid Selection", "Please select the first data in the queue.")
            #     tb1.selection_remove(selected)  # Deselect the invalid selection
            # else:
            #     # If the first item is selected, store it for transferring
                selected_item = tb1.item(selected, "values")

    tb1.bind("<<TreeviewSelect>>", on_item_selected)

    # Buttons---------------------------------------------------------------------------------
    table_btn = ctk.CTkFrame(promisorry, width=700, height=0, fg_color='transparent')
    table_btn.pack(side='bottom', fill='x', pady=10)

    call_btn = ctk.CTkButton(table_btn, text='Call ticket', height=35, text_color='#fff', command=call_ticket)
    call_btn.pack(side='left', padx=10)


    promisorry.mainloop()
