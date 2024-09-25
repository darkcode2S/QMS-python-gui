import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import re
from db import create_connection
from mysql.connector import Error
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

#display data in each tables of students by course from database
def fetch_students_by_course(course_name):
    connection = create_connection()  # Create the database connection
    if connection is None:
        print("Failed to connect to the database.")
        return []

    cursor = connection.cursor()
    query = "SELECT school_id, full_name, course, year_level FROM student WHERE course = %s"  # Query to fetch students by course
    cursor.execute(query, (course_name,))  # Execute the query with the course name

    students = cursor.fetchall()  # Fetch all results
    cursor.close()
    connection.close()
    return students  # Return the list of students


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
            table.pack_forget()
            tab_view.pack(fill="both", expand=True)  # Show the tab view for students
            
            # Clear previous data in each student tab
            for tab_name in tab_list:
                tables[tab_name].delete(*tables[tab_name].get_children())

            # Fetch students from the database for each course and insert into the relevant table
            for course_name in tab_list:
                students_data = fetch_students_by_course(course_name)  # Fetch data for each course
                
                if students_data:
                    for student in students_data:
                        # Insert each student record into the corresponding Treeview
                        tables[course_name].insert("", "end", values=student)
                else:
                    print(f"No students found for the course: {course_name}")



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


#ACTION FROM DATABASE++++++++++++++++++
# Placeholder functions for the buttons
def add_record():
    # Function to add a record to the database based on the current selected table
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()

    # Get the main window's geometry
    x = admin.winfo_x()
    y = admin.winfo_y()
    width = 300  # Desired width of the pop-up window
    height = 350  # Desired height of the pop-up window
    # Calculate the center position
    x_position = x + (admin.winfo_width() // 2) - (width // 2)
    y_position = y + (admin.winfo_height() // 2) - (height // 2)

    if dropdown_var.get() == "Students":
        add_window = ctk.CTkToplevel(admin)
        add_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
        add_window.title("Add Student")
        add_window.iconbitmap("old-logo.ico")
        add_window.grab_set()  # Make the window modal

        add_window.resizable(False, False)
        # Create a frame for the input fields
        input_frame = ctk.CTkFrame(add_window, fg_color='transparent')
        input_frame.pack(expand=True, fill='y', pady=(10, 0))  # Center the frame in the window

        add_label = ctk.CTkLabel(input_frame, text='Add Record', font=ctk.CTkFont(size=20, weight="bold"))
        add_label.pack(padx=10, pady=10)

        # Create input fields for adding a student
        input_schoolid = ctk.CTkEntry(input_frame, width=250, placeholder_text='School ID')
        input_schoolid.pack(padx=10, pady=10)
        input_fullname = ctk.CTkEntry(input_frame, width=250, placeholder_text='Full name')
        input_fullname.pack(padx=10, pady=10)

        dropdown_course = ctk.StringVar(value="Select Course")
        dropdown_layout = ctk.CTkOptionMenu(input_frame, variable=dropdown_course, width=250,
                              values=[
                                      "BSCS", 
                                      'BS-CRIM', 
                                      "BSSW", 
                                      "BSEE",
                                      'BSMT',
                                      'BSM',
                                      'BEED',
                                      'BSED',
                                      'BSBA',
                                      'BSHM',
                                      'BSA',
                                      'BAPS'], 
                              fg_color="#fff",
                              text_color="#000",
                              dropdown_fg_color="#fff",
                              button_color="orange",
                              dropdown_hover_color="orange",
                              button_hover_color="#de9420")
        dropdown_layout.pack(padx=10, pady=10)

        dropdown_year = ctk.StringVar(value="Select Year & level")
        dropdown_level = ctk.CTkOptionMenu(input_frame, variable=dropdown_year, width=250,
                              values=[
                                      "1st Year", 
                                      '2nd Year', 
                                      "3rd Year", 
                                      "4rth Year",
                                      '5th Year',
                                      '6th Year',
                                      '7th Year',
                                      '8th Year',
                                      '9th Year',
                                      '10th Year'], 
                              fg_color="#fff",
                              text_color="#000",
                              dropdown_fg_color="#fff",
                              button_color="orange",
                              dropdown_hover_color="orange",
                              button_hover_color="#de9420")
        dropdown_level.pack(padx=10, pady=10)

        # Button to add the student record
        add_button = ctk.CTkButton(input_frame, text="Add", command=lambda: insert_student_data(
            input_schoolid.get(),
            input_fullname.get(),
            dropdown_course.get(),
            dropdown_year.get(),
            connection,
            cursor,
            add_window  # Pass the add window to close it later
        ))
        add_button.pack(padx=10, pady=10)


        
    # elif not dropdown_var.get() == "Students":
    #     messagebox.showerror("Add Failed", "Only Students, Members and Passwords table can Add Record.")
        
#Database query for add students
def insert_student_data(school_id, fullname, course, year, connection, cursor, add_window):
    try:
        school_id_pattern = r'^\d{2}-\d{4}$'
              # Input validation
        if not school_id or not fullname or not course or not year:
            messagebox.showerror("Add Record", "All fields are required.")
            return      
        elif course == 'Select Course' or year == 'Select Year & level':
           messagebox.showerror("Add Record", "All fields are required.")
           return
              
        # Validate school_id format
        elif not re.match(school_id_pattern, school_id):
            messagebox.showerror("Add Record", "Error: Invalid school ID format. Please use 'XX-XXXX' format (e.g., '00-0000').")
            return  # Exit the function if validation fails  
          

        query = "INSERT INTO student (school_id, full_name, course, year_level) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (school_id, fullname, course, year))
        connection.commit()  # Commit the changes to the database
        print("Record added successfully")
        update_table("Students")
        add_window.destroy()  # Close the add window
        cursor.close()
        connection.close()
    except Error as err:  # Catch MySQL specific errors
        print(f"Error: {err}")  # Handle MySQL errors as warnings
        

    # elif dropdown_var.get() == "Queue":
    #     queue_window = ctk.CTkToplevel(admin)
    #     queue_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
    #     queue_window.title("Add Queue")
    #     queue_window.iconbitmap("old-logo.ico")
    #     queue_window.grab_set()  # Make the window modal

    #     # Create a frame for the input fields
    #     input_frame = ctk.CTkFrame(queue_window)
    #     input_frame.pack(expand=True)  # Center the frame in the window

    #     # Create input fields for adding a queue
    #     input_queue_number = ctk.CTkEntry(input_frame)
    #     input_queue_number.pack(padx=10, pady=10)  # Centering
    #     input_queue_name = ctk.CTkEntry(input_frame)
    #     input_queue_name.pack(padx=10, pady=10)  # Centering
    #     input_details = ctk.CTkEntry(input_frame)
    #     input_details.pack(padx=10, pady=10)  # Centering
    #     input_affiliation = ctk.CTkEntry(input_frame)
    #     input_affiliation.pack(padx=10, pady=10)  # Centering
    #     input_ticket_number = ctk.CTkEntry(input_frame)
    #     input_ticket_number.pack(padx=10, pady=10)  # Centering
    #     input_time = ctk.CTkEntry(input_frame)
    #     input_time.pack(padx=10, pady=10)  # Centering
    #     input_completed = ctk.CTkEntry(input_frame)
    #     input_completed.pack(padx=10, pady=10)  # Centering

    #     # Button to add the queue record
    #     add_button = ctk.CTkButton(input_frame, text="Add Queue")
    #     add_button.pack(padx=10, pady=10)  # Centering

    # cursor.close()
    # connection.close()


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