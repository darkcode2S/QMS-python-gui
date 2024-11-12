import tkinter as tk
import customtkinter as ctk
from PIL import Image

from center_window import center_window

# Initialize the main window
root = ctk.CTk()  # Use customtkinter's window for CTk elements
root.title("Queue Management System")
root.iconbitmap("old-logo.ico")
center_window(800, 500, root)

# Create the main frame that will contain the boxes and the title
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

# Create a title frame and place it at the top of main_frame
title_frame = tk.Frame(main_frame)
title_frame.pack(pady=(20, 50))  # Add padding to position it higher

# Load and display the logo image in the title_frame
logo_icon = ctk.CTkImage(light_image=Image.open("old-logo.png"),
                         dark_image=Image.open("old-logo.png"),
                         size=(80, 80))  # Resize to 60x60 pixels

logo_ncmc = ctk.CTkLabel(title_frame, image=logo_icon, text="")
logo_ncmc.pack(pady=(0, 5))  # Add some padding below the image

# Create the welcome label in the title_frame and center it
welcome_label = tk.Label(title_frame, text="Welcome to NCMC Queue Management System", font=("Helvetica", 16, "bold"))
welcome_label.pack()

# Create a sub-frame for centering the boxes within it
center_frame = tk.Frame(main_frame)
center_frame.pack(expand=True)

# Create a frame for each box and label
box1_frame = tk.Frame(center_frame)
box1_frame.pack(side=tk.LEFT, padx=20, pady=10)

box2_frame = tk.Frame(center_frame)
box2_frame.pack(side=tk.LEFT, padx=20, pady=10)

box3_frame = tk.Frame(center_frame)
box3_frame.pack(side=tk.LEFT, padx=20, pady=10)

# Create three boxes (labels) and pack them inside their respective frames
box1 = tk.Label(box1_frame, text="Box 1", width=20, height=10, bg="lightblue")
box1.pack()

box2 = tk.Label(box2_frame, text="Box 2", width=20, height=10, bg="lightgreen")
box2.pack()

box3 = tk.Label(box3_frame, text="Box 3", width=20, height=10, bg="lightcoral")
box3.pack()

# Add descriptive labels under each box
label1 = tk.Label(box1_frame, text="Administration", font=("Helvetica", 12))
label1.pack(pady=10)

label2 = tk.Label(box2_frame, text="Queue Display", font=("Helvetica", 12))
label2.pack(pady=10)

label3 = tk.Label(box3_frame, text="User", font=("Helvetica", 12))
label3.pack(pady=10)

# Run the main loop
root.mainloop()
