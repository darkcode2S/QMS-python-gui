import customtkinter as ctk
from tkinter import messagebox
import bcrypt
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

    window_width = 320
    window_height = 350

    screen_width = log_in_window.winfo_screenwidth()
    screen_height = log_in_window.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    log_in_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    photo = ctk.CTkImage(light_image=Image.open("old-logo.png"),
                          dark_image=Image.open("old-logo.png"),
                          size=(80, 80))

    # Center the username entry, password entry, and button
    frame = ctk.CTkFrame(log_in_window, fg_color='transparent')
    frame.pack(expand=True, fill='both')

    image_label = ctk.CTkLabel(frame, image=photo, text="")  # Empty text to display only the image
    image_label.pack(pady=10)

    username_label = ctk.CTkLabel(frame, text='Username', width=280, anchor='w')
    username_label.pack()

    username_input = ctk.CTkFrame(frame, fg_color='transparent', border_width=2, border_color='lightgray')
    username_input.pack(pady=(0, 10), fill='x', padx=20)

    username_entry = ctk.CTkEntry(username_input,
                                  width=300, 
                                  placeholder_text='Username', 
                                  border_width=0,
                                  fg_color='transparent')
    username_entry.pack(padx=5, pady=5)

    password_label = ctk.CTkLabel(frame, text='Password', width=280, anchor='w')
    password_label.pack()

    # Create password entry
    password_input = ctk.CTkFrame(frame, fg_color='transparent', border_width=2, border_color='lightgray')
    password_input.pack(pady=(0, 10), fill='x', padx=20)

    password_entry = ctk.CTkEntry(password_input, 
                                  width=230, 
                                  show="*", 
                                  placeholder_text='Password', 
                                  border_width=0,
                                  fg_color='transparent')
    password_entry.pack(side='left', pady=5, padx=(5,0))

    # Load icons for showing/hiding password
    eye_open_image = ctk.CTkImage(light_image=Image.open("eye_open.png"),
                                   dark_image=Image.open("eye_open.png"),
                                   size=(20, 20))
    eye_closed_image = ctk.CTkImage(light_image=Image.open("eye_closed.png"),
                                     dark_image=Image.open("eye_closed.png"),
                                     size=(20, 20))

    # Function to toggle password visibility
    def toggle_password_visibility():
        if password_entry.cget('show') == "*":
            password_entry.configure(show="")
            eye_button.configure(image=eye_open_image)
        else:
            password_entry.configure(show="*")
            eye_button.configure(image=eye_closed_image)

    # Button to toggle password visibility
    eye_button = ctk.CTkButton(password_input, 
                               fg_color='transparent', 
                               image=eye_closed_image, 
                               text="",
                               hover='transparent',
                               command=toggle_password_visibility, 
                               width=30)
    eye_button.pack(side="right", pady=5, padx=(0,5))

    # Create custom button with orange background color
    button = ctk.CTkButton(frame, width=280, text="Log in",
                           corner_radius=6, 
                           height=35,
                           fg_color="#d68b26", 
                           hover_color="#a45e14",
                           command=lambda: log_in(username_entry.get(), password_entry.get(), log_in_window, root))
    button.pack(pady=15, padx=20)

    def on_enter(event):
        button.invoke()  # Simulate button click

    # Bind Enter key to the sign-in window
    log_in_window.bind('<Return>', on_enter)
    # Make the sign-in window modal
    log_in_window.grab_set()  # Prevent interaction with other windows

# Function to handle sign-in logic to database
def log_in(username, password, log_in_window, root):
    from counter_staff_profile_interface import counter_staff_home

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

                    connection.close()
                    cursor.close()
                else:
                    messagebox.showerror("Login Failed", "Incorrect password.")
            # Check if user is found in operator table
            elif operator_user:
                stored_password = operator_user[6]  # Assuming password is the sixth field
                op_name = operator_user[1]
                op_area = operator_user[3]

                if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):  # Compare passwords
                    role = operator_user[7]  # Assuming role is the seventh field
                    messagebox.showinfo("Success", f"Logged in successfully as {role.capitalize()}!")
                    # log_in_window.destroy()
                    root.destroy()
                    counter_staff_home(op_name, op_area) 
                    
                    connection.close()
                    cursor.close()
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
