import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from db import create_connection

def open_login_window(root):
    # Create sign-in window
    log_in_window = ctk.CTkToplevel(root)
    log_in_window.geometry("400x300")
    log_in_window.title("Log in")
    log_in_window.iconbitmap("old-logo.ico")
 

    # Disable maximize button
    log_in_window.resizable(False, False)  # Disable resizing

    window_width = 400
    window_height = 300

    screen_width = log_in_window.winfo_screenwidth()
    screen_height = log_in_window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    log_in_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    photo = ctk.CTkImage(light_image=Image.open("old-logo.png"),
                                  dark_image=Image.open("old-logo.png"),
                                  size=(50, 50))
    image_label = ctk.CTkLabel(log_in_window, image=photo, text="")  # Empty text to display only the image
    image_label.pack(pady=(20, 10))

    # Center the username entry, password entry, and button
    frame = ctk.CTkFrame(log_in_window, width=400, height=300, fg_color="transparent")
    frame.pack(expand=True)

    # Center elements vertically in the frame
    frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
    frame.grid_columnconfigure(0, weight=1)

    username_entry = ctk.CTkEntry(frame, width=220, placeholder_text='Username')
    username_entry.grid(row=1, column=0, pady=12)

    password_entry = ctk.CTkEntry(frame, width=220, show="*", placeholder_text='Password')
    password_entry.grid(row=2, column=0, pady=12)

    # Create custom button with orange background color
    button = ctk.CTkButton(frame, width=100, text="Log in", 
                           corner_radius=6, 
                           fg_color='orange', 
                           hover_color="#de9420",
                           command=lambda: log_in(username_entry.get(), password_entry.get(), log_in_window, root))
    button.grid(row=3, column=0, pady=15)

    def on_enter(event):
        button.invoke()  # Simulate button click

    # Bind Enter key to the sign-in window
    log_in_window.bind('<Return>', on_enter)
    # Make the sign-in window modal
    log_in_window.grab_set()  # Prevent interaction with other windows

# # Function to handle sign-in logic to database
def log_in(username, password, log_in_window, root):
    connection = create_connection()
    cursor = None

    try:
        if connection:
            cursor = connection.cursor()

            # Validate input
            if not username and not password:
                messagebox.showerror("Login Failed", "Username and password are required.")
                return
            elif not username:
                messagebox.showerror("Login Failed", "Username is required.")
                return
            elif not password:
                messagebox.showerror("Login Failed", "Password is required.")
                return

            # Query to check if the user is in the admin table
            query = "SELECT * FROM admin WHERE username = %s"
            cursor.execute(query, (username,))
            admin_user = cursor.fetchone()

            # Query to check if the user is in the operator table
            query = "SELECT * FROM operator WHERE username = %s"
            cursor.execute(query, (username,))
            operator_user = cursor.fetchone()

            # Check if user is found in admin table
            if admin_user:
                if admin_user[2] == password:  # Assuming password is the third field
                    role = admin_user[3]  # Assuming role is the fourth field
                    messagebox.showinfo("Success", f"Logged in successfully as {role.capitalize()}!")
                    log_in_window.destroy()
                    root.destroy()
                    import admin_dashboard  # Redirect to admin dashboard
                else:
                    messagebox.showerror("Login Failed", "Incorrect password.")
            # Check if user is found in operator table
            elif operator_user:
                if operator_user[6] == password:  # Assuming password is the sixth field
                    role = operator_user[7]  # Assuming role is the seventh field
                    messagebox.showinfo("Success", f"Logged in successfully as {role.capitalize()}!")
                    log_in_window.destroy()
                    root.destroy()
                    import operator_dashboard  # Redirect to operator dashboard              
                else:
                    messagebox.showerror("Login Failed", "Incorrect password.")
            else:
                messagebox.showerror("Login Failed", "Member does not exist.")

        else:
            messagebox.showerror("Error", "Failed to connect to the database.")

    except Exception as e:
        print(f"Error during sign-in: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
