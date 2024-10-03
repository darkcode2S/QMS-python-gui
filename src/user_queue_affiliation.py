import customtkinter as ctk
from PIL import Image 
from student_queue_input_id import input_id_student
from user_queue_staff_input_id import satff_input_id
from user_queue_visitor import visitor_queue

def affiliation(root, button_text):
    user_aff = ctk.CTkToplevel(root)
    user_aff.title("Queue affiliation")
    user_aff.iconbitmap("old-logo.ico")

    # Set appearance mode and color theme (Light/Dark modes)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    # Center the window on the screen
    window_width = 800
    window_height = 440
    screen_width = user_aff.winfo_screenwidth()
    screen_height = user_aff.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    user_aff.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create the main frame for content
    frame = ctk.CTkFrame(user_aff, width=700, height=300, fg_color="transparent")
    frame.pack(expand=True)


    # Create a bold heading label under the image
    sub_label = ctk.CTkLabel(frame, text="PLEASE CLICK THE APPROPRIATE KEY FOR",
                                font=ctk.CTkFont(size=30, weight="bold"), 
                                text_color="#000000", anchor="center")
    sub_label.pack(pady=(0, 10))
    sub_label = ctk.CTkLabel(frame, text="YOUR AFFILIATION",
                                font=ctk.CTkFont(size=30, weight="bold"), 
                                text_color="#000000", anchor="center")
    sub_label.pack(pady=(0, 10))

    button_frame = ctk.CTkFrame(frame, width=700, height=300, fg_color="transparent")
    button_frame.pack(expand=True, fill='x')

    proc_button = ctk.CTkButton(button_frame, 
                                text='Student', 
                                fg_color='#d68b26',
                                border_color='#000', 
                                border_width=1, 
                                font=ctk.CTkFont(size=20, weight="bold"),
                                height=80,
                                command=lambda: student(),
                                width=300)
    proc_button.pack(pady=20, side="left", padx=20)

    proc_button = ctk.CTkButton(button_frame , 
                                text='Staff/Faculty',  
                                border_color='#000', 
                                border_width=1,
                                fg_color='#d68b26',
                                height=80, 
                                font=ctk.CTkFont(size=20, weight="bold"),
                                command=lambda: staff(),
                                width=300)
    proc_button.pack(pady=20, side="right", padx=20)

    proc_button = ctk.CTkButton(frame , 
                                text='Visitor',  
                                border_color='#000', 
                                border_width=1,
                                fg_color='#d68b26',
                                height=80, 
                                font=ctk.CTkFont(size=20, weight="bold"),
                                command=lambda: visitor(),
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
        user_aff.destroy()

    def student():
        select_student = 'Student'
        input_id_student(root, button_text, select_student)

    def staff():
        satff_input_id(root)

    def visitor():
        visitor_queue(root)


    user_aff.grab_set()


