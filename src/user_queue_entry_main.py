import customtkinter as ctk
from PIL import Image
from user_queue_transaction import transaction

user = ctk.CTk()
user.title("Entry Queue")
user.iconbitmap("old-logo.ico")

# Set appearance mode and color theme (Light/Dark modes)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Center the window on the screen
window_width = 800
window_height = 440
screen_width = user.winfo_screenwidth()
screen_height = user.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
user.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the main frame for content
frame = ctk.CTkFrame(user, width=700, height=300, fg_color="transparent")
frame.pack(expand=True)

photo = ctk.CTkImage(light_image=Image.open("old-logo.png"),
                     dark_image=Image.open("old-logo.png"),
                     size=(150, 150))  

image_label = ctk.CTkLabel(frame, image=photo, text="" , anchor='center')  
image_label.pack(pady=(20, 20), side='left', padx=10)


# Create a bold heading label under the image
heading_label = ctk.CTkLabel(frame, text="Welcome!",
                             font=ctk.CTkFont(size=80, weight="bold"), 
                             text_color="#000000", anchor="center")
heading_label.pack(pady=(130, 0), padx=(0,20))
sub_label = ctk.CTkLabel(frame, text="Join the Entry Queue Here.",
                             font=ctk.CTkFont(size=30, weight="bold"), 
                             text_color="#000000", anchor="center")
sub_label.pack(pady=(0, 10))

button_frame = ctk.CTkFrame(frame, width=700, height=300, fg_color="transparent")
button_frame.pack(expand=True, fill='x')

proc_button = ctk.CTkButton(button_frame , height=35, text='Proceed', fg_color='#d68b26', command=lambda:open_transaction_window())
proc_button.pack(pady=40, side="left", padx=20)

def open_transaction_window():
    transaction(user)


user.mainloop()


