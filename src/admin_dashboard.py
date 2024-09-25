import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from admin_tables import queue_table,  password_table

# Initialize the main application window
admin = ctk.CTk()
admin.geometry("1000x500")
admin.title("Admin")
admin.iconbitmap("old-logo.ico")

# Set appearance mode and color theme (Light/Dark modes)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")
# Center the window on the screen
window_width = 1000
window_height = 500
screen_width = admin.winfo_screenwidth()
screen_height = admin.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
admin.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Show the sensitive data warning message
messagebox.showinfo("Info", "Please be aware that you are accessing sensitive data.")

# Create the main frame for content
main_frame = ctk.CTkFrame(admin, width=700, height=300)
main_frame.pack(side="left", expand=True, fill="both")

# Sidebar frame
sidebar_frame = ctk.CTkFrame(main_frame, width=200, height=300, fg_color="transparent")
sidebar_frame.pack(side="left", fill="both", padx="20")

table_label = ctk.CTkLabel(
    sidebar_frame,
    text="Tables",
    font=ctk.CTkFont(),
    text_color="#000000",
    anchor="w"  # Use "w" for west (left)
)
table_label.pack(anchor="w", padx=(8, 0), pady=(10, 0))

# Create dropdown menu for selecting members, queue, and passwords
dropdown_var = ctk.StringVar(value="Select Option")
dropdown = ctk.CTkOptionMenu(sidebar_frame, variable=dropdown_var, 
                              values=['Select Option', "Queue", 'Students', 
                                      "Members", "Passwords"], 
                              fg_color="#fff",
                              text_color="#000",
                              dropdown_fg_color="#fff",
                              button_color="orange",
                              dropdown_hover_color="orange",
                              button_hover_color="#de9420",
                              command=lambda choice: update_table(choice))
dropdown.pack(pady=(0, 10))

# Create buttons for adding, deleting, and updating records
add_button = ctk.CTkButton(sidebar_frame, text="Add Record", text_color="#000", fg_color="white", hover_color="#de9420", command=lambda: add_record())
add_button.pack(pady=10)

remove_button = ctk.CTkButton(sidebar_frame, text="Remove Record", text_color="#000", fg_color="white", hover_color="#de9420", command=lambda: remove_record())
remove_button.pack(pady=10)

update_button = ctk.CTkButton(sidebar_frame, text="Update Record", text_color="#000", fg_color="white", hover_color="#de9420", command=lambda: update_record())
update_button.pack(pady=10)

logout_button = ctk.CTkButton(sidebar_frame, text="Log out", text_color="#000", fg_color="lightblue", hover_color="#de9420", command=lambda: confirm_logout())
logout_button.pack(side="bottom", pady='30')

# Table Frame
table_frame = ctk.CTkFrame(main_frame, width=500, height=300)
table_frame.pack(side="right", fill="both", expand=True, padx=(0, 20))

# TabView for students
tab_view = ctk.CTkTabview(table_frame, width=500, height=300, anchor="nw")
tab_view.pack_forget()  # Initially hide the tab view

# Dictionary to store table references for each tab
tables = {}

# List of tabs to create dynamically
tab_list = ["BSCS", "BS-CRIM", "BSSW", "BSEE", "BSMT", "BSM", "BEED", "BSED", "BSBA", "BSHM", "BSA", "BAPS"]

# Function to dynamically create tabs and tables
def create_tabs():
    for tab_name in tab_list:
        tab_view.add(tab_name)  # Add the tab
        table_student = ttk.Treeview(tab_view.tab(tab_name), show="headings")
        table_student['columns'] = ('School ID', 'Full name', 'Course', 'Year&level')
        table_student.column("#0", width=0, stretch="no")
        table_student.column("School ID", anchor="center", width=80)
        table_student.column("Full name", anchor="center", width=80)
        table_student.column("Course", anchor="center", width=80)
        table_student.column("Year&level", anchor="center", width=80)
        
        table_student.heading("#0", text="")
        table_student.heading("School ID", text="School ID")
        table_student.heading("Full name", text="Full name")
        table_student.heading("Course", text="Course")
        table_student.heading("Year&level", text="Year & Level")     
        table_student.pack(fill="both", expand=True, pady=(0, 20))
        tables[tab_name] = table_student  # Store the table reference for each tab

create_tabs()  # Create tabs and tables dynamically

table = ttk.Treeview(table_frame)
table.pack(fill="both", expand=True, pady=20)


tab_member = ctk.CTkTabview(table_frame, width=500, height=300, anchor="nw")
tab_member.add("School Staff")  # Add the BSCS tab
tab_member.add("School Faculty")  # Add the CRIM tab
tab_member.pack_forget()  # Initially hide the tab view

# Create Treeview tables inside each Tab
# Create Treeview tables inside each Tab
school_staff = ttk.Treeview(tab_member.tab("School Staff"), show="headings") 
school_staff['columns'] = ('School ID', 'Full name', 'Office', 'Role')    
school_staff.column("#0", width=0, stretch="no")
school_staff.column("School ID", anchor="s", width=80)
school_staff.column("Full name", anchor="w", width=80)
school_staff.column("Office", anchor="w", width=80)
school_staff.column("Role", anchor="w", width=80)

school_staff.heading("#0", text="", anchor="center")
school_staff.heading("School ID", text="School ID", anchor="center")
school_staff.heading("Full name", text="Full name")
school_staff.heading("Office", text="Office")
school_staff.heading("Role", text="Role")
school_staff.pack(fill="both", expand=True, pady=(0, 20))
# Disable column dragging

school_faculty = ttk.Treeview(tab_member.tab("School Faculty"), show="headings") 
school_faculty['columns'] = ('School ID', 'Full name', 'Department', 'Role')    
school_faculty.column("#0", width=0, stretch="no")
school_faculty.column("School ID", anchor="s", width=80)
school_faculty.column("Full name", anchor="w", width=80)
school_faculty.column("Department", anchor="w", width=80)
school_faculty.column("Role", anchor="w", width=80)

school_faculty.heading("#0", text="", anchor="center")
school_faculty.heading("School ID", text="School ID", anchor="center")
school_faculty.heading("Full name", text="Full name")
school_faculty.heading("Department", text="Department")
school_faculty.heading("Role", text="Role")
school_faculty.pack(fill="both", expand=True, pady=(0, 20))
# Disable column dragging
# school_faculty.bind("<Button-1>", lambda e: "break")  # Prevents dragging of the headers

# Function to add unique data to a table
def add_unique_data_to_table(tree, data):
    existing_data = [tree.item(item, 'values') for item in tree.get_children()]
    
    for record in data:
        if record not in existing_data:  # Check if the record is already present
            tree.insert("", "end", values=record)  # Insert only if not present

# Update table based on selection
def update_table(choice):
    # Clear current table data
    for item in table.get_children():
        table.delete(item)
    
    # Hide the tab views initially
    tab_view.pack_forget()
    tab_member.pack_forget()
    table.pack(fill="both", expand=True, pady=20)

    # Configure the appropriate columns for the selected table
    if choice == "Members":
        table.pack_forget()  # Hide the treeview
        tab_member.pack(fill="both", expand=True)  # Show the tab view

        # Add sample data to each tab's table
        staff_data = [('21-3434', "Roselyn Basan", 'BSCS', '4th year', '098473834')]
        for item in school_staff.get_children():
            school_staff.delete(item)
        for record in staff_data:
            school_staff.insert("", "end", values=record)

        faculty_data = [('21-3434', "john doe", 'BSCS', '4th year', '098473834')]
        for item in school_faculty.get_children():
            school_faculty.delete(item)
        for record in faculty_data:
            school_faculty.insert("", "end", values=record)

    elif choice == "Queue":
        tab_member.pack_forget()
        define_queue_columns()
        queue_data = [(1, "Queue 1", "Details 1", "Affiliation 1fdgfdgdgf", 100, "10:30", "No"),
                      (2, "Queue 2", "Details 2", "Affiliation 2", 101, "11:00", "Yes")]
        for queue in queue_data:
            table.insert("", "end", values=queue)

    elif choice == "Passwords":
        tab_member.pack_forget()
        define_password_columns()
        passwords_data = [(1, "User1", "Password1"),
                          (2, "User2", "Password2")]
        for password in passwords_data:
            table.insert("", "end", values=password)
            
    elif choice == "Students":
        table.pack_forget()  # Hide the treeview
        tab_view.pack(fill="both", expand=True)  # Show the tab view for students

        # Add sample data to each tab's table
        bscs_data = [('21-3434', "Roselyn Basan", 'BSCS', '4th year', '098473834')]
        add_unique_data_to_table(tables["BSCS"], bscs_data)

        crim_data = [('21-3434', "John Doe", 'BS-CRIM', '3rd year', '0912345678')]
        add_unique_data_to_table(tables["BS-CRIM"], crim_data)

    elif choice == "Select Option":
        # Clear current table data
        for item in table.get_children():
            table.delete(item)
         # Clear the headings
        table["columns"] = ()
        table.heading("#0", text="")  # Hide the default column header


# Function to define columns for the queue table
def define_queue_columns():
    queue_table(table)

# Function to define columns for the password table
def define_password_columns():
    password_table(table)

# Placeholder functions for the buttons
def add_record():
    print("Add record")

def remove_record():
    print("Remove record")

def update_record():
    print("Update record")
    
def confirm_logout():
    response = messagebox.askyesno("Log out", "Are you sure you want to log out?")
    if response:
        # Code to log out the user
        admin.destroy()
    else:
        print("Logout canceled.")


admin.mainloop()