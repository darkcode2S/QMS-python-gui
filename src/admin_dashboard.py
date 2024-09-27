import customtkinter as ctk
from tkinter import END, Event, StringVar, ttk
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
window_height = 550
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

update_button = ctk.CTkButton(sidebar_frame, text="Update Record", text_color="#000", fg_color="white", hover_color="#de9420", command=lambda: update_record())
update_button.pack(pady=10)

remove_button = ctk.CTkButton(sidebar_frame, text="Remove Record", text_color="#000", fg_color="white", hover_color="#de9420", command=lambda: remove_record())
remove_button.pack(pady=10)

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


selected_item_values = None  # Variable to store the currently selected item values

# Function to handle selection from the table
def on_item_selected(event, tab_name):
    global selected_item_values  # Use the global variable to store selected values
    selected_table = tables[tab_name]  # Get the table reference
    selected_item = selected_table.selection()  # Get selected item
    if selected_item:
        selected_item_values = selected_table.item(selected_item, "values")  # Get the values of the selected item
        print(f"Selected Item from {tab_name}: {selected_item_values}")  # Process or display the selected values


# Function to dynamically create tabs and tables
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
    
    # Bind the selection event to the table
    table_student.bind("<<TreeviewSelect>>", lambda event, tab_name=tab_name: on_item_selected(event, tab_name))
    
    tables[tab_name] = table_student  # Store the table reference for each tab


 # Create tabs and tables dynamically

table = ttk.Treeview(table_frame)
table.pack(fill="both", expand=True, pady=20)


# Create Treeview tables inside each Tab
# TabView for Members
tab_member = ctk.CTkTabview(table_frame, width=500, height=300, anchor="nw")
tab_member.pack_forget()  # Initially hide the tab view

# Dictionary to store table references for each tab
member_tables = {}

# List of tabs to create dynamically
member_list = ['School staff', 'School faculty']


select_member_value = None  # Variable to store the currently selected item values

# Function to handle selection from the table
def member_selected(event, member_name):
    global select_member_value  # Use the global variable to store selected values
    selected_table = member_tables[member_name]  # Get the table reference
    selected_item = selected_table.selection()  # Get selected item
    if selected_item:
        select_member_value = selected_table.item(selected_item, "values")  # Get the values of the selected item
        print(f"Selected Item from {member_name}: {select_member_value}")  # Process or display the selected values


# Function to dynamically create tabs and tables for members
for member_name in member_list:
    tab_member.add(member_name)  # Add the tab
    table_member = ttk.Treeview(tab_member.tab(member_name), show="headings")
    table_member['columns'] = ('School ID', 'Full name', 'Affiliation', 'Role', 'Office')
    
    table_member.column("#0", width=0, stretch="no")
    table_member.column("School ID", anchor="center", width=80)
    table_member.column("Full name", anchor="center", width=80)
    table_member.column("Affiliation", anchor="center", width=80)
    table_member.column("Role", anchor="center", width=80)
    table_member.column("Office", anchor="center", width=80)
    
    table_member.heading("#0", text="")
    table_member.heading("School ID", text="School ID")
    table_member.heading("Full name", text="Full name")
    table_member.heading("Affiliation", text="Affiliation")
    table_member.heading("Role", text="Role")
    table_member.heading("Office", text="Office")
    
    table_member.pack(fill="both", expand=True, pady=(0, 20))
    
    # Bind the selection event to the table
    table_member.bind("<<TreeviewSelect>>", lambda event, member_name=member_name: member_selected(event, member_name))
    
    member_tables[member_name] = table_member  # Store the table reference for each tab

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

def fetch_members_data(member_item_name):
    connection = create_connection()  # Create the database connection
    if connection is None:
        print("Failed to connect to the database.")
        return []

    cursor = connection.cursor()
    query = "SELECT school_id, full_name, affiliation, role, office FROM member WHERE office = %s"  # Query to fetch students by course
    cursor.execute(query, (member_item_name,))  # Execute the query with the course name

    member = cursor.fetchall()  # Fetch all results
    cursor.close()
    connection.close()
    return member  # Return the list of students



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
        table.pack_forget()
        tab_member.pack(fill="both", expand=True)  # Show the tab view for students
            
        # Clear previous data in each student tab
        for member_name in member_list:
            member_tables[member_name].delete(*member_tables[member_name].get_children())

            # Fetch students from the database for each course and insert into the relevant table
        for member_item_name in member_list:
            member_data = fetch_members_data(member_item_name)  # Fetch data for each course
                
            if member_data:
                for member in member_data:
                     # Insert each student record into the corresponding Treeview
                    member_tables[member_item_name].insert("", "end", values=member)
            else:
                messagebox.showinfo('Show info',f"No students found for the course: {member_item_name}")

    elif choice == "Queue":
        tab_member.pack_forget()
        define_queue_columns()
        queue_data = [(1, "Queue 1", "Details 1", "Affiliation 1fdgfdgdgf", 100, "10:30", "No"),
                      (2, "Queue 2", "Details 2", "Affiliation 2", 101, "11:00", "Yes")]
        for queue in queue_data:
            table.insert("", "end", values=queue)

    elif choice == "Passwords":
        # tab_member.pack_forget()
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
                    messagebox.showinfo('Show info',f"No students found for the course: {course_name}")



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


#ACTION FROM DATABASE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
    width = 320  # Desired width of the pop-up window
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
        add_button = ctk.CTkButton(input_frame, text="Add",width=250, command=lambda: insert_student_data(
            input_schoolid.get(),
            input_fullname.get(),
            dropdown_course.get(),
            dropdown_year.get(),
            connection,
            cursor,
            add_window  # Pass the add window to close it later
        ))
        add_button.pack(padx=10, pady=10)
    # else:
    #     messagebox.showerror("Add Failed", "Only Students, Members and Passwords table can Add Record.")
       
    # elif not dropdown_var.get() == "Students":
    #     messagebox.showerror("Add Failed", "Only Students, Members and Passwords table can Add Record.")
    elif dropdown_var.get() == "Members":
        member_window = ctk.CTkToplevel(admin)
        member_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
        member_window.title("Add member")
        member_window.iconbitmap("old-logo.ico")
        member_window.grab_set()  # Make the window modal

        member_window.resizable(False, False)

        # Create a frame for the input fields
        member_frame = ctk.CTkFrame(member_window, width=250)
        member_frame.pack(expand=True, fill='x')  # Center the frame in the window

        # Create input fields for adding a member
        member_heading = ctk.CTkLabel(member_frame, text='Add member record')
        member_heading.pack(padx=10)
        member_id = ctk.CTkEntry(member_frame, width=250, placeholder_text='School ID')
        member_id.pack(padx=10, pady=10)  # Centering
        member_name = ctk.CTkEntry(member_frame, width=250, placeholder_text='Full name')
        member_name.pack(padx=10, pady=10)  # Centering
        member_aff = ctk.CTkEntry(member_frame, width=250, placeholder_text='Affiliation')
        member_aff.pack(padx=10, pady=10)  # Centering
        member_role = ctk.CTkEntry(member_frame, width=250, placeholder_text='Role')
        member_role.pack(padx=10, pady=10)  # Centering
        dropdown_member = ctk.StringVar(value="Select office")
        dropdown_member_layout = ctk.CTkOptionMenu(member_frame, variable=dropdown_member, width=250,
                              values=[
                                      'Select office',
                                      "School staff", 
                                      'School faculty'
                                     ], 
                              fg_color="#fff",
                              text_color="#000",
                              dropdown_fg_color="#fff",
                              button_color="orange",
                              dropdown_hover_color="orange",
                              button_hover_color="#de9420")
        dropdown_member_layout.pack(padx=10, pady=10)
        # Button to add the queue record
        add_member = ctk.CTkButton(member_frame, text="Add",width=250,
                                   command=lambda: insert_member_data(
                                        member_id.get(),
                                        member_name.get(),
                                        member_aff.get(),
                                        member_role.get(),
                                        dropdown_member.get(),
                                        connection,
                                        cursor,
                                        member_window  # Pass the add window to close it later
                                    ))  # Centering
        add_member.pack(padx=10, pady=10)
        
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
        update_table("Students")
        add_window.destroy()  # Close the add window
        messagebox.showinfo('Success',"Record added successfully")
        cursor.close()
        connection.close()
    except Error as err:  # Catch MySQL specific errors
        print(f"Error: {err}")  # Handle MySQL errors as warning

def insert_member_data(school_id, fullname, affiliation, role, office, connection, cursor, member_window):
    try:
        school_id_pattern = r'^\d{2}-\d{4}$'
              # Input validation
        if not school_id or not fullname or not affiliation or not role or not office:
            messagebox.showerror("Add Record", "All fields are required.")
            return      
        elif office == 'Select office':
           messagebox.showerror("Add member Record", "All fields are required.")
           return
              
        # Validate school_id format
        elif not re.match(school_id_pattern, school_id):
            messagebox.showerror("Add member Record", "Error: Invalid school ID format. Please use 'XX-XXXX' format (e.g., '00-0000').")
            return  # Exit the function if validation fails  
          

        query = "INSERT INTO member (school_id, full_name, affiliation, role, office) VALUES (%s, %s, %s, %s,%s)"
        cursor.execute(query, (school_id, fullname, affiliation, role, office))
        connection.commit()  # Commit the changes to the database
        update_table("Members")
        member_window.destroy()  # Close the add window
        messagebox.showinfo('Success',"Record member added successfully")
        cursor.close()
        connection.close()
    except Error as err:  # Catch MySQL specific errors
        print(f"Error: {err}")  # Handle MySQL errors as warning
        

#update record
def update_record():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()

    x = admin.winfo_x()
    y = admin.winfo_y()
    width = 320  # Desired width of the pop-up window
    height = 380  # Desired height of the pop-up window
    # Calculate the center position
    x_position = x + (admin.winfo_width() // 2) - (width // 2)
    y_position = y + (admin.winfo_height() // 2) - (height // 2)

    if dropdown_var.get() == "Students":
        global selected_item_values  # Access the selected item values
        if selected_item_values is None:
            messagebox.showwarning("Warning","No item selected for update.")
            return  # Exit if no item is selected
        # Create a modal update window
        update_window = ctk.CTkToplevel(admin)
        update_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
        update_window.title("Update Student")
        update_window.iconbitmap("old-logo.ico")
        update_window.grab_set()  # Make the window modal
        update_window.resizable(False, False)

        # Create a frame for the input fields
        update_member_frame = ctk.CTkFrame(update_window, fg_color='transparent')
        update_member_frame.pack(expand=True, fill='y', pady=(10, 0))  # Center the frame in the window

        update_label = ctk.CTkLabel(update_member_frame, text='Update record', font=ctk.CTkFont(size=20, weight="bold"))
        update_label.pack(padx=10, pady=10)

        # Create input fields for updating a student and set their initial values
        schoolid_text = ctk.CTkLabel(update_member_frame, text='School ID', width=250, text_color='#979490')
        schoolid_text.pack(padx=(0,190))
        update_schoolid = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='School ID', fg_color='lightgray')
        update_schoolid.pack(padx=10)
        update_schoolid.insert(0, selected_item_values[0])  # Set the School ID
        update_schoolid.configure(state="disabled")

        fullname_text = ctk.CTkLabel(update_member_frame, text='Full name', width=250, text_color='#979490')
        fullname_text.pack(padx=(0,190))
        update_fullname = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='Full name')
        update_fullname.pack(padx=10)
        update_fullname.insert(0, selected_item_values[1])  # Set the Full name

        course_text = ctk.CTkLabel(update_member_frame, text='Course', width=250, text_color='#979490')
        course_text.pack(padx=(0,200))
        update_course = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='Course')
        update_course.pack(padx=10)
        update_course.insert(0, selected_item_values[2])  # Set the Course

        year_text = ctk.CTkLabel(update_member_frame, text='Year level', width=250, text_color='#979490')
        year_text.pack(padx=(0,190))
        update_year = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='Year & level')
        update_year.pack(padx=10)
        update_year.insert(0, selected_item_values[3])  # Set the Year & Level

        # Update button with functionality
        update_button = ctk.CTkButton(
            update_member_frame,
            width=250,
            text='Update record',
            command=lambda: save_changes_to_database(
                update_schoolid.get(),
                update_fullname.get(),
                update_course.get(),
                update_year.get(),
                connection,
                cursor,
                update_window  # Pass the update window to close it later
            )
        )
        update_button.pack(padx=10, pady=20)
    # else:
    #     messagebox.showerror("Update Failed", "Only Students, Members and Passwords table can Update record.")
    elif dropdown_var.get() == "Members":
        x = admin.winfo_x()
        y = admin.winfo_y()
        width = 320  # Desired width of the pop-up window
        height = 400  # Desired height of the pop-up window
        # Calculate the center position
        x_position = x + (admin.winfo_width() // 2) - (width // 2)
        y_position = y + (admin.winfo_height() // 2) - (height // 2)

        global select_member_value  # Access the selected item values
        if select_member_value is None:
            messagebox.showwarning("Warning","No item selected for update.")
            return  # Exit if no item is selected
        # Create a modal update window
        update_member = ctk.CTkToplevel(admin)
        update_member.geometry(f"{width}x{height}+{x_position}+{y_position}")
        update_member.title("Update member")
        update_member.iconbitmap("old-logo.ico")
        update_member.grab_set()  # Make the window modal
        update_member.resizable(False, False)

        # Create a frame for the input fields
        update_member_frame = ctk.CTkFrame(update_member, fg_color='transparent')
        update_member_frame.pack(expand=True, fill='y', pady=(10, 0))  # Center the frame in the window

        update_label = ctk.CTkLabel(update_member_frame, text='Update record', font=ctk.CTkFont(size=20, weight="bold"))
        update_label.pack()

        # Create input fields for updating a student and set their initial values
        schoolid_text = ctk.CTkLabel(update_member_frame, text='School ID', width=250, text_color='#979490')
        schoolid_text.pack(padx=(0,190))
        update_schoolid = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='School ID', fg_color='lightgray')
        update_schoolid.pack(padx=10)
        update_schoolid.insert(0, select_member_value[0])  # Set the School ID
        update_schoolid.configure(state="disabled")

        fullname_text = ctk.CTkLabel(update_member_frame, text='Full name', width=250, text_color='#979490')
        fullname_text.pack(padx=(0,190))
        update_fullname = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='Full name')
        update_fullname.pack(padx=10)
        update_fullname.insert(0, select_member_value[1])  # Set the Full name

        course_text = ctk.CTkLabel(update_member_frame, text='Affiliation', width=250, text_color='#979490')
        course_text.pack(padx=(0,200))
        update_course = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='Affiliation')
        update_course.pack(padx=10)
        update_course.insert(0, select_member_value[2])  # Set the Course

        year_text = ctk.CTkLabel(update_member_frame, text='Role', width=250, text_color='#979490')
        year_text.pack(padx=(0,190))
        update_year = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='Role')
        update_year.pack(padx=10)
        update_year.insert(0, select_member_value[3])  # Set the Year & Level

        office_text = ctk.CTkLabel(update_member_frame, text='Office', width=250, text_color='#979490')
        office_text.pack(padx=(0,190))
        office_member = ctk.CTkEntry(update_member_frame, width=250, placeholder_text='Office')
        office_member.pack(padx=10)
        office_member.insert(0, select_member_value[4])  # Set the Year & Level

        # Update button with functionality
        update_button = ctk.CTkButton(
            update_member_frame,
            width=250,
            text='Update record',
            command=lambda: save_changes_member(
                update_schoolid.get(),
                update_fullname.get(),
                update_course.get(),
                update_year.get(),
                office_member.get(),
                connection,
                cursor,
                update_member  # Pass the update window to close it later
            )
        )
        update_button.pack(padx=10, pady=20)

#Action of update in databse
def save_changes_to_database(school_id, fullname, course, year, conn, cursor, update):
    try:

        year_format = [
                '1st Year', 
                '2nd Year', 
                '3rd Year',
                '4rth Year', 
                '5th Year', 
                '6th Year', 
                '7th Year', 
                '8th Year', 
                '9th Year',
                '10th Year'
                ]
         # Input validation
        if not school_id or not fullname or not course or not year:
            messagebox.showerror("Update record", "All fields are required.")
            return      
        elif course not in tab_list:
           messagebox.showerror("Update record", "Please input valid Course")
           return
        elif year not in year_format:
           messagebox.showerror("Update record", "Please input valid Year level")
           return                             

        query = "UPDATE student SET school_id = %s, full_name = %s, course =%s, year_level =%s WHERE school_id = %s"
        cursor.execute(query, (school_id, fullname, course, year, school_id))
        conn.commit()  # Commit the changes to the database       
        update_table("Students")
        update.destroy()  # Close the add window
        messagebox.showinfo('Success',"Record update successfully")
        cursor.close()
        conn.close()
    except Error as err:  # Catch MySQL specific errors
        print(f"Error: {err}")  # Handle MySQL errors as warnings

def save_changes_member(school_id, fullname, affiliation, role, office, conn, cursor, update):
    try:

        office_format = [
                'School staff', 
                'School faculty'
                ]
         # Input validation
        if not school_id or not fullname or not affiliation or not role or not office:
            messagebox.showerror("Update record member", "All fields are required.")
            return      
        
        elif office not in office_format:
           messagebox.showerror("Update record member", "Please input valid office")
           return                             

        query = "UPDATE member SET school_id = %s, full_name = %s, affiliation =%s, role =%s, office =%s WHERE school_id = %s"
        cursor.execute(query, (school_id, fullname, affiliation, role, office, school_id))
        conn.commit()  # Commit the changes to the database       
        update_table("Members")
        update.destroy()  # Close the add window
        messagebox.showinfo('Success',"Record update successfully")
        cursor.close()
        conn.close()
    except Error as err:  # Catch MySQL specific errors
        print(f"Error: {err}")  # Handle MySQL errors as warnings



def remove_record():
    connection = create_connection()
    if connection is None:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()

    x = admin.winfo_x()
    y = admin.winfo_y()
    width = 320  # Desired width of the pop-up window
    height = 380  # Desired height of the pop-up window
    # Calculate the center position
    x_position = x + (admin.winfo_width() // 2) - (width // 2)
    y_position = y + (admin.winfo_height() // 2) - (height // 2)

    if dropdown_var.get() == "Students":
        global selected_item_values  # Access the selected item values
        if selected_item_values is None:
           messagebox.showwarning("Warning","No item selected for remove.")
           return  # Exit if no item is selected
        # Create a modal update window
        remove_window = ctk.CTkToplevel(admin)
        remove_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
        remove_window.title("Remove Student")
        remove_window.iconbitmap("old-logo.ico")
        remove_window.grab_set()  # Make the window modal
        remove_window.resizable(False, False)

        # Create a frame for the input fields
        remove_frame = ctk.CTkFrame(remove_window, fg_color='transparent')
        remove_frame.pack(expand=True, fill='y', pady=(10, 0))  # Center the frame in the window

        remove_label = ctk.CTkLabel(remove_frame, text='Remove record', font=ctk.CTkFont(size=20, weight="bold"))
        remove_label.pack(padx=10, pady=10)

        # Create input fields for updating a student and set their initial values
        remove_text = ctk.CTkLabel(remove_frame, text='School ID', width=250, text_color='#979490')
        remove_text.pack(padx=(0,190))
        remove_schoolid = ctk.CTkEntry(remove_frame, width=250, placeholder_text='School ID', border_width=0, fg_color='transparent')
        remove_schoolid.pack(padx=10)
        remove_schoolid.insert(0, selected_item_values[0])  # Set the School ID
        remove_schoolid.configure(state="disabled")

        remove_text = ctk.CTkLabel(remove_frame, text='Full name', width=250, text_color='#979490')
        remove_text.pack(padx=(0,190))
        remove_fullname = ctk.CTkEntry(remove_frame, width=250, placeholder_text='Full name', border_width=0, fg_color='transparent')
        remove_fullname.pack(padx=10)
        remove_fullname.insert(0, selected_item_values[1])  # Set the Full name
        remove_fullname.configure(state="disabled")

        remove_text = ctk.CTkLabel(remove_frame, text='Course', width=250, text_color='#979490')
        remove_text.pack(padx=(0,200))
        remove_course = ctk.CTkEntry(remove_frame, width=250, placeholder_text='Course', border_width=0, fg_color='transparent')
        remove_course.pack(padx=10)
        remove_course.insert(0, selected_item_values[2])  # Set the Course
        remove_course.configure(state="disabled")      

        remove_text = ctk.CTkLabel(remove_frame, text='Year level', width=250, text_color='#979490')
        remove_text.pack(padx=(0,190))
        remove_year = ctk.CTkEntry(remove_frame, width=250, placeholder_text='Year level', border_width=0, fg_color='transparent')
        remove_year.pack(padx=10)
        remove_year.insert(0, selected_item_values[3])  # Set the Year & Level
        remove_year.configure(state="disabled")

        # Update button with functionality
        remove_button = ctk.CTkButton(
            remove_frame,
            width=250,
            text='Remove record',
            command=lambda: remove_data_from_database(
                remove_schoolid.get(),
                connection,
                cursor,
                remove_window  # Pass the remove window to close it later
            )
        )
        remove_button.pack(padx=10, pady=20)
    # else:
    #     messagebox.showerror("Remove Failed", "Only Students, Members and Passwords table can Remove Record.")
    elif dropdown_var.get() == "Members":
        x = admin.winfo_x()
        y = admin.winfo_y()
        width = 320  # Desired width of the pop-up window
        height = 400  # Desired height of the pop-up window
        # Calculate the center position
        x_position = x + (admin.winfo_width() // 2) - (width // 2)
        y_position = y + (admin.winfo_height() // 2) - (height // 2)

        global select_member_value  # Access the selected item values
        if select_member_value is None:
           messagebox.showwarning("Warning","No item selected for remove.")
           return  # Exit if no item is selected
        # Create a modal update window
        remove_window = ctk.CTkToplevel(admin)
        remove_window.geometry(f"{width}x{height}+{x_position}+{y_position}")
        remove_window.title("Remove Student")
        remove_window.iconbitmap("old-logo.ico")
        remove_window.grab_set()  # Make the window modal
        remove_window.resizable(False, False)

        # Create a frame for the input fields
        remove_frame = ctk.CTkFrame(remove_window, fg_color='transparent')
        remove_frame.pack(expand=True, fill='y', pady=(10, 0))  # Center the frame in the window

        remove_label = ctk.CTkLabel(remove_frame, text='Remove record', font=ctk.CTkFont(size=20, weight="bold"))
        remove_label.pack()

        # Create input fields for updating a student and set their initial values
        remove_text = ctk.CTkLabel(remove_frame, text='School ID', width=250, text_color='#979490')
        remove_text.pack(padx=(0,190))
        remove_schoolid = ctk.CTkEntry(remove_frame, width=250, placeholder_text='School ID', border_width=0, fg_color='transparent')
        remove_schoolid.pack(padx=10)
        remove_schoolid.insert(0, select_member_value[0])  # Set the School ID
        remove_schoolid.configure(state="disabled")

        remove_text = ctk.CTkLabel(remove_frame, text='Full name', width=250, text_color='#979490')
        remove_text.pack(padx=(0,190))
        remove_fullname = ctk.CTkEntry(remove_frame, width=250, placeholder_text='Full name', border_width=0, fg_color='transparent')
        remove_fullname.pack(padx=10)
        remove_fullname.insert(0, select_member_value[1])  # Set the Full name
        remove_fullname.configure(state="disabled")

        remove_text = ctk.CTkLabel(remove_frame, text='Affiliation', width=250, text_color='#979490')
        remove_text.pack(padx=(0,200))
        remove_course = ctk.CTkEntry(remove_frame, width=250, placeholder_text='Course', border_width=0, fg_color='transparent')
        remove_course.pack(padx=10)
        remove_course.insert(0, select_member_value[2])  # Set the Course
        remove_course.configure(state="disabled")      

        remove_text = ctk.CTkLabel(remove_frame, text='Role', width=250, text_color='#979490')
        remove_text.pack(padx=(0,190))
        remove_year = ctk.CTkEntry(remove_frame, width=250, placeholder_text='Year level', border_width=0, fg_color='transparent')
        remove_year.pack(padx=10)
        remove_year.insert(0, select_member_value[3])  # Set the Year & Level
        remove_year.configure(state="disabled")

        remove_text = ctk.CTkLabel(remove_frame, text='Office', width=250, text_color='#979490')
        remove_text.pack(padx=(0,190))
        remove_year = ctk.CTkEntry(remove_frame, width=250, placeholder_text='Year level', border_width=0, fg_color='transparent')
        remove_year.pack(padx=10)
        remove_year.insert(0, select_member_value[4])  # Set the Year & Level
        remove_year.configure(state="disabled")

        # Update button with functionality
        remove_button = ctk.CTkButton(
            remove_frame,
            width=250,
            text='Remove record',
            command=lambda: remove_member_data(
                remove_schoolid.get(),
                connection,
                cursor,
                remove_window  # Pass the remove window to close it later
            )
        )
        remove_button.pack(padx=10, pady=20)


def remove_data_from_database(school_id, conn, cursor, remove):
    remove_res = messagebox.askyesno("Confirm", "Are you sure to delete this record")
    if remove_res:
        try:
            # Prepare and execute the DELETE query
            query = "DELETE FROM `student` WHERE school_id = %s"
            cursor.execute(query, (school_id,))  # Use a tuple with only the school_id
            conn.commit()  # Commit the changes to the database

            print("Record removed successfully")
            update_table("Students")  # Update the displayed table (assuming this is defined elsewhere)
            
            remove.destroy()  # Close the remove window
        except Error as err:  # Catch MySQL specific errors
            print(f"Error: {err}")  # Handle MySQL errors as warnings
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the connection
    else:
        print("Remove canceled.")

def remove_member_data(school_id, conn, cursor, remove):
    remove_res = messagebox.askyesno("Confirm", "Are you sure to delete this record")
    if remove_res:
        try:
            # Prepare and execute the DELETE query
            query = "DELETE FROM `member` WHERE school_id = %s"
            cursor.execute(query, (school_id,))  # Use a tuple with only the school_id
            conn.commit()  # Commit the changes to the database

            print("Record removed successfully")
            update_table("Members")  # Update the displayed table (assuming this is defined elsewhere)         
            remove.destroy()  # Close the remove window
        except Error as err:  # Catch MySQL specific errors
            print(f"Error: {err}")  # Handle MySQL errors as warnings
        finally:
            cursor.close()  # Close the cursor
            conn.close()    # Close the connection
        remove.destroy()
    else:
        remove.destroy()
        print("Remove canceled.")

    
def confirm_logout():
    response = messagebox.askyesno("Log out", "Are you sure you want to log out?")
    if response:
        # Code to log out the user
        admin.destroy()
    else:
        print("Logout canceled.")


admin.mainloop()