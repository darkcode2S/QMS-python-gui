import customtkinter as ctk

operator = ctk.CTk()
operator.geometry("800x400")
operator.title("Operator")
operator.iconbitmap("old-logo.ico")

# Set appearance mode and color theme (Light/Dark modes)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Center the window on the screen
window_width = 800
window_height = 440
screen_width = operator.winfo_screenwidth()
screen_height = operator.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
operator.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create the main frame for content
frame = ctk.CTkFrame(operator, width=700, height=300, fg_color="transparent")
frame.pack(expand=True)


# Create a bold heading label under the image
heading_label = ctk.CTkLabel(frame, text="Welcome Operator",
                             font=ctk.CTkFont(size=50, weight="bold"), 
                             text_color="#000000", anchor="center")
heading_label.pack(pady=(10, 10))

# # Create the 'Get Started' button with a Bootstrap-like style and center it
# get_started_button = ctk.CTkButton(frame, text="Sign In", width=120, height=40, 
#                                    fg_color="orange", hover_color="#fccd84", text_color="white", 
#                                    font=ctk.CTkFont(size=14, weight="bold"),
#                                   )  # Call the defined function
# get_started_button.pack(pady=20)

# def on_enter(event):
#     get_started_button.invoke()  # Simulate button click

    
# # Bind Enter key to the sign-in window
# operator.bind('<Return>', on_enter)
# Start the main loop
operator.mainloop()


