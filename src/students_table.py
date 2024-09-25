import customtkinter as ctk
from PIL import Image
from log_in import open_login_window

# Function to open a new sign-in window and show a message box
def open_new_window():
    ctk.CTkMessageBox.show_info("Info", "Opening the login window...")
    open_login_window(root)

# Function to exit the application
def on_exit():
    root.quit()

# Initialize the main window
root = ctk.CTk()
root.geometry("800x400")
root.title("Queue Management System")
root.iconbitmap("old-logo.ico")

# Set appearance mode and color theme (Light/Dark modes)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Center the window on the screen
window_width = 800
window_height = 440
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load the logo image
photo = ctk.CTkImage(light_image=Image.open("old-logo.png"),
                     dark_image=Image.open("old-logo.png"),
                     size=(150, 150))

# Create the main frame for content
frame = ctk.CTkFrame(root, width=700, height=300, fg_color="transparent")
frame.pack(expand=True)

# Add the image on top of the label
image_label = ctk.CTkLabel(frame, image=photo, text="")  # Empty text to display only the image
image_label.pack(pady=(20, 10))

# Create a bold heading label under the image
heading_label = ctk.CTkLabel(frame, text="NCMC Data Queue System",
                              font=ctk.CTkFont(size=50, weight="bold"), 
                              text_color="#000000", anchor="center")
heading_label.pack(pady=(10, 10))

# Button frame
button_frame = ctk.CTkFrame(root, width=700, height=300, fg_color="transparent")
button_frame.pack(expand=True)

# 'Log In' Button
button_login = ctk.CTkButton(button_frame, text="Log in", width=120, height=30, 
                              fg_color="orange", hover_color="#de9420", text_color="white", 
                              font=ctk.CTkFont(size=12, weight="bold"),
                              command=open_new_window)  # Call the defined function
button_login.pack(pady=20, side="left", padx=20)

# 'Exit' Button
button_exit = ctk.CTkButton(button_frame, text="Exit", width=120, height=30, 
                             fg_color="orange", hover_color="#de9420", text_color="white", 
                             font=ctk.CTkFont(size=12, weight="bold"),
                             command=on_exit)  # Call the defined function
button_exit.pack(pady=20, side="left", padx=20)

# Bind Enter key to the sign-in window
root.bind('<Return>', lambda event: button_login.invoke())  # Simulate button click

# Start the main loop
root.mainloop()
