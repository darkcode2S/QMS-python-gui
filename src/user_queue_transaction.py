import customtkinter as ctk
from PIL import Image 
from purpose_of_visit import purpose_visit_student, purpose_visit_staff, purpose_visit_visitor

def transaction(root):
    user_transaction = ctk.CTkToplevel(root)
    user_transaction.title("Queue transaction")
    user_transaction.iconbitmap("old-logo.ico")

    # Set appearance mode and color theme (Light/Dark modes)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    # Center the window on the screen
    window_width = 800
    window_height = 440
    screen_width = user_transaction.winfo_screenwidth()
    screen_height = user_transaction.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    user_transaction.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the main frame for content
    frame = ctk.CTkFrame(user_transaction, width=700, height=300, fg_color="transparent")
    frame.pack(expand=True)


    # Create a bold heading label under the image
    sub_label = ctk.CTkLabel(frame, text="PLEASE CLICK THE PROPER KEY FOR",
                                font=ctk.CTkFont(size=30, weight="bold"), 
                                text_color="#000000", anchor="center")
    sub_label.pack(pady=(0, 10))
    sub_label = ctk.CTkLabel(frame, text="YOUR DESIRED TRANSACTION",
                                font=ctk.CTkFont(size=30, weight="bold"), 
                                text_color="#000000", anchor="center")
    sub_label.pack(pady=(0, 10))

    button_frame = ctk.CTkFrame(frame, width=700, height=300, fg_color="transparent")
    button_frame.pack(expand=True, fill='x')

    proc_button = ctk.CTkButton(button_frame, 
                                text='CASHIER SERVICE', 
                                fg_color='#d68b26',
                                border_color='#000', 
                                border_width=1, 
                                font=ctk.CTkFont(size=20, weight="bold"),
                                height=80, 
                                command=lambda:cashier_service(),
                                width=300)
    proc_button.pack(pady=20, side="left", padx=20)

    proc_button = ctk.CTkButton(button_frame , 
                                text='PROMISORRY NOTE COORDINATOR',  
                                border_color='#000', 
                                border_width=1,
                                fg_color='#d68b26',
                                height=80, 
                                font=ctk.CTkFont(size=20, weight="bold"),
                                command=lambda:promisorry_note(),
                                width=300)
    proc_button.pack(pady=20, side="right", padx=20)

    proc_button = ctk.CTkButton(frame , 
                                text='SCHOLARSHIP COORDINATOR',  
                                border_color='#000', 
                                border_width=1,
                                fg_color='#d68b26',
                                height=80, 
                                font=ctk.CTkFont(size=20, weight="bold"),
                                command=lambda:scholarship_coordinator(),
                                width=300)
    proc_button.pack(pady=20, padx=20)

    proc_button = ctk.CTkButton(frame , 
                                text='Cancel', 
                                border_color='#000', 
                                border_width=1,
                                height=35,
                                fg_color='#fff',
                                command=lambda: cancel_button(),
                                text_color='#000')
    proc_button.pack(pady=20, padx=20)


    def cancel_button():
        user_transaction.destroy()

    def cashier_service():
        button_text = 'Cashier Service'
        purpose_visit_student(root, button_text)

    def promisorry_note():
        button_text = 'Promisorry note coordinator'
        purpose_visit_staff(root, button_text)

    def scholarship_coordinator():
        button_text = 'Scholarship coordinator'
        purpose_visit_visitor(root, button_text)

    user_transaction.grab_set()




