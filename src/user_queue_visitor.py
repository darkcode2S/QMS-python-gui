import customtkinter as ctk
from PIL import Image

def visitor_queue(root):
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

    cancel_button = ctk.CTkButton(button_frame , height=35, text='Cancel', fg_color='#fff', text_color='#000', border_width=1, border_color='#000', 
                                  command=lambda:cancel())
    cancel_button.pack(side="left", padx=20)

    create_button = ctk.CTkButton(button_frame , height=35, text='Create Ticket', fg_color='#fff', text_color='#000', border_width=1, border_color='#000')
    create_button.pack(side="left", padx=20)



    def cancel():
        user_visitor.destroy()


    user_visitor.grab_set()


