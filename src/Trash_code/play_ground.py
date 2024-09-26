import tkinter
import customtkinter

# customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()  # Creating custom tkinter window
# app.geometry("600x440")
# app.title('Login')

# # Center the window on the screen
# window_width = 600
# window_height = 440

# screen_width = app.winfo_screenwidth()
# screen_height = app.winfo_screenheight()

# x = (screen_width // 2) - (window_width // 2)
# y = (screen_height // 2) - (window_height // 2)

# app.geometry(f"{window_width}x{window_height}+{x}+{y}")

# # Creating custom frame
# frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
# frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
# l2.place(x=50, y=45)

# entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
# entry1.place(x=50, y=110)

# entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
# entry2.place(x=50, y=165)

# # Create custom button with orange background color
# button1 = customtkinter.CTkButton(master=frame, width=220, text="Sign in", corner_radius=6, fg_color='orange', hover_color="#b99153")
# button1.place(x=50, y=240)

# app.mainloop() Playgroudn====================================================================================

# class MyFrame(customtkinter.CTkFrame):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # add widgets onto the frame, for example:
#         self.label = customtkinter.CTkLabel(self)
#         self.label.grid(row=3, column=4, padx=20)


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x200")
#         self.grid_rowconfigure(0, weight=1)  # configure grid system
#         self.grid_columnconfigure(0, weight=1)

#         self.my_frame = MyFrame(master=self)
#         self.my_frame.grid(row=4, column=4, padx=20, pady=20, sticky="nsew")


# app = App()
# app.mainloop()

# import tkinter as tk
# from tkinter import ttk

# # Create the main window
# root = tk.Tk()
# root.title("Treeview Example")

# # Create a Treeview widget
# tree = ttk.Treeview(root, columns=("Name", "Age", "Gender"), show='headings')

# # Define headings
# tree.heading("Name", text="Name")
# tree.heading("Age", text="Age")
# tree.heading("Gender", text="Gender")

# # Insert sample data
# tree.insert("", tk.END, values=("John Doe", 30, "Male"))
# tree.insert("", tk.END, values=("Jane Smith", 28, "Female"))
# tree.insert("", tk.END, values=("Mike Johnson", 35, "Male"))

# tree.pack()

# # Function to get selected item
# def get_selected_item():
#     selected_item = tree.selection()  # Get selected item
#     if selected_item:
#         item = tree.item(selected_item)
#         values = item['values']  # Get the values of the selected item
#         print("Selected item:", values)
#     else:
#         print("No item selected")

# # Button to trigger the selection
# btn = tk.Button(root, text="Get Selected Item", command=get_selected_item)
# btn.pack()

# root.mainloop()

import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Multiple Tables Example")

# Create a list to store the Treeview widgets (tables)
tables = []

# Column headers
columns = ("School ID", "Full Name", "Course", "Year Level")

# Sample data for the tables
data = [
    [("12-2323", "John Doe", "Computer Science", "3rd Year"),
     ("13-1122", "Jane Smith", "Business Management", "2nd Year")],
    [("14-5544", "Mike Johnson", "Engineering", "1st Year"),
     ("15-9988", "Linda Lee", "Architecture", "4th Year")],
    [("16-6633", "Chris White", "Computer Science", "3rd Year"),
     ("17-4455", "Sara Brown", "Law", "2nd Year")],
    [("18-7788", "James Green", "Medicine", "4th Year"),
     ("19-2299", "Emily Black", "Nursing", "1st Year")]
]

# Create 4 tables
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Treeview to Entry Example")

# Create Entry widgets for ID, Name, and Age
entry_id = tk.Entry(root, width=20)
entry_name = tk.Entry(root, width=20)
entry_age = tk.Entry(root, width=20)

entry_id.grid(row=0, column=1, padx=10, pady=10)
entry_name.grid(row=1, column=1, padx=10, pady=10)
entry_age.grid(row=2, column=1, padx=10, pady=10)

# Create labels
tk.Label(root, text="ID").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Age").grid(row=2, column=0, padx=10, pady=10)

# Create Treeview
tree = ttk.Treeview(root, columns=("ID", "Name", "Age"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# Add some example data to the Treeview
data = [("1", "John Doe", "25"),
        ("2", "Jane Smith", "30"),
        ("3", "Mike Lee", "22")]

for item in data:
    tree.insert("", "end", values=item)

tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Function to get the selected item and populate the Entry fields
def on_tree_select(event):
    selected_item = tree.selection()[0]  # Get selected item
    values = tree.item(selected_item, "values")  # Get values of the selected row
    
    # Populate the Entry fields
    entry_id.delete(0, tk.END)
    entry_id.insert(0, values[0])
    
    entry_name.delete(0, tk.END)
    entry_name.insert(0, values[1])
    
    entry_age.delete(0, tk.END)
    entry_age.insert(0, values[2])

# Bind the treeview selection event to the on_tree_select function
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Run the main loop
root.mainloop()

