import importlib
import time
import customtkinter as ctk
import tkinter as tk
from PIL import Image
from tkinter import messagebox
from user_queue_affiliation import affiliation


def purpose_visit_student(root, button_text):
        # Create a Toplevel window (like a dialog)
        dialog = ctk.CTkToplevel(root)
        dialog.title("Cashier service")

        dialog.resizable(False, False)

        window_width = 500
        window_height = 300
        screen_width = dialog.winfo_screenwidth()
        screen_height = dialog.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        dialog.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a label for the dialog with a cool font and color
        label = ctk.CTkLabel(dialog, text="Choose a purpose of visit", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)
        
        #radio frame
        visit_frame = ctk.CTkFrame(dialog, fg_color='transparent')
        visit_frame.pack(fill='x')

        visit_frame.columnconfigure(0, weight=1)
        visit_frame.columnconfigure(1, weight=1)
        visit_frame.rowconfigure(0, weight=1)
        visit_frame.rowconfigure(1, weight=1)
        visit_frame.rowconfigure(2, weight=1)

        # Create a StringVar to hold the selected radio button value
        selected_option = tk.StringVar(value="Tuition fee")

        # Create the radio buttons with custom styling---------------------------------------------------
        radio1 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Tuition fee", 
                                    variable=selected_option, 
                                    value="Tuition fee", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio1.pack(padx=30,pady=10, anchor='w')
        radio1.grid(row=0, column=0, padx=30,pady=10, sticky='w')

        radio2 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Registration fee", 
                                    variable=selected_option, 
                                    value="Registration fee",
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio2.pack(padx=30,pady=10, anchor='w')
        radio2.grid(row=1, column=0, padx=30,pady=10, sticky='w')

        radio3 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Research fee", 
                                    variable=selected_option, 
                                    value="Research fee", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio3.pack(padx=30,pady=10, anchor='w')
        radio3.grid(row=2, column=0, padx=30,pady=10, sticky='w')

        radio4 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Endorsement fee", 
                                    variable=selected_option, 
                                    value="Endorsement fee", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio1.pack(padx=30,pady=10, anchor='w')
        radio4.grid(row=0, column=1, padx=30,pady=10, sticky='w')

        radio5 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Graduation fee", 
                                    variable=selected_option, 
                                    value="Graduation fee",
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio2.pack(padx=30,pady=10, anchor='w')
        radio5.grid(row=1, column=1, padx=30,pady=10, sticky='w')

        radio6 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Others", 
                                    variable=selected_option, 
                                    value="Others", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio3.pack(padx=30,pady=10, anchor='w')
        radio6.grid(row=2, column=1, padx=30,pady=10, sticky='w')

        # Function to handle confirmation----------------------------------------------------------
        def confirm_selection():
            purpose = selected_option.get()
            dialog.destroy()  # Close the dialog window
            affiliation(root, button_text, purpose)

        # Create a button to confirm selection with custom styling
        confirm_button = ctk.CTkButton(dialog, 
                                    text="Confirm", 
                                    command=confirm_selection,
                                    fg_color="#d68b26", 
                                    hover_color="#a45e14")
        confirm_button.pack(pady=(50,0))

        dialog.grab_set()


def purpose_visit_staff(root, button_text):
        # Create a Toplevel window (like a dialog)
        dialog2 = ctk.CTkToplevel(root)
        dialog2.title("Promisorry note coordinator")

        dialog2.resizable(False, False)

        window_width = 500
        window_height = 300
        screen_width = dialog2.winfo_screenwidth()
        screen_height = dialog2.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        dialog2.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a label for the dialog2 with a cool font and color
        label = ctk.CTkLabel(dialog2, text="Choose a purpose of visit", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)
        
        #radio frame
        visit_frame = ctk.CTkFrame(dialog2, fg_color='transparent')
        visit_frame.pack(fill='x')

        visit_frame.columnconfigure(0, weight=1)
        visit_frame.columnconfigure(1, weight=1)
        visit_frame.rowconfigure(0, weight=1)
        visit_frame.rowconfigure(1, weight=1)
        visit_frame.rowconfigure(2, weight=1)

        # Create a StringVar to hold the selected radio button value
        selected_option = tk.StringVar(value="Scholarship application")

        # Create the radio buttons with custom styling---------------------------------------------------
        radio1 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Scholarship application", 
                                    variable=selected_option, 
                                    value="Scholarship application", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio1.pack(padx=30,pady=10, anchor='w')
        radio1.grid(row=0, column=0, padx=30,pady=10, sticky='w')

        radio2 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Payroll signing", 
                                    variable=selected_option, 
                                    value="Payroll signing",
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio2.pack(padx=30,pady=10, anchor='w')
        radio2.grid(row=1, column=0, padx=30,pady=10, sticky='w')

        radio3 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Scholarship inquiry", 
                                    variable=selected_option, 
                                    value="Scholarship inquiry", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio3.pack(padx=30,pady=10, anchor='w')
        radio3.grid(row=2, column=0, padx=30,pady=10, sticky='w')

        radio4 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Scholarship update", 
                                    variable=selected_option, 
                                    value="Scholarship update", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio1.pack(padx=30,pady=10, anchor='w')
        radio4.grid(row=0, column=1, padx=30,pady=10, sticky='w')

        radio5 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Others", 
                                    variable=selected_option, 
                                    value="Others",
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio2.pack(padx=30,pady=10, anchor='w')
        radio5.grid(row=1, column=1, padx=30,pady=10, sticky='w')

        # Function to handle confirmation----------------------------------------------------------
        def confirm_selection():
            purpose = selected_option.get()
            dialog2.destroy()  # Close the dialog2 window
            affiliation(root, button_text, purpose)

        # Create a button to confirm selection with custom styling
        confirm_button = ctk.CTkButton(dialog2, 
                                    text="Confirm", 
                                    command=confirm_selection,
                                    fg_color="#d68b26", 
                                    hover_color="#a45e14")
        confirm_button.pack(pady=(50,0))

        dialog2.grab_set()

def purpose_visit_visitor(root, button_text):
        # Create a Toplevel window (like a dialog)
        dialog3 = ctk.CTkToplevel(root)
        dialog3.title("Scholarship coordinator")

        dialog3.resizable(False, False)

        window_width = 300
        window_height = 230
        screen_width = dialog3.winfo_screenwidth()
        screen_height = dialog3.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        dialog3.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a label for the dialog3 with a cool font and color
        label = ctk.CTkLabel(dialog3, text="Choose a purpose of visit", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=20)
        
        #radio frame
        visit_frame = ctk.CTkFrame(dialog3, fg_color='transparent')
        visit_frame.pack(fill='x')

        visit_frame.columnconfigure(0, weight=1)
        visit_frame.rowconfigure(0, weight=1)
        visit_frame.rowconfigure(1, weight=1)

        # Create a StringVar to hold the selected radio button value
        selected_option = tk.StringVar(value="Promisorry note")

        # Create the radio buttons with custom styling---------------------------------------------------
        radio1 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Promisorry note", 
                                    variable=selected_option, 
                                    value="Promisorry note", 
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio1.pack(padx=30,pady=10, anchor='w')
        radio1.grid(row=0, column=0, padx=30,pady=10, sticky='w')

        radio2 = ctk.CTkRadioButton(visit_frame, 
                                    text="  Others", 
                                    variable=selected_option, 
                                    value="Others",
                                    fg_color="#d68b26", 
                                    hover_color="#d68b26")
        # radio2.pack(padx=30,pady=10, anchor='w')
        radio2.grid(row=1, column=0, padx=30,pady=10, sticky='w')


        # Function to handle confirmation----------------------------------------------------------
        def confirm_selection():
            purpose = selected_option.get()
            dialog3.destroy()  # Close the dialog3 window
            affiliation(root, button_text, purpose)

        # Create a button to confirm selection with custom styling
        confirm_button = ctk.CTkButton(dialog3, 
                                    text="Confirm", 
                                    command=confirm_selection,
                                    fg_color="#d68b26", 
                                    hover_color="#a45e14")
        confirm_button.pack(pady=(20,0))

        dialog3.grab_set()
