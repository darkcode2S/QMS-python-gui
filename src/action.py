import customtkinter as ctk
import tkinter as ttk

from db import create_connection
    


# Function to add a record to the database based on the current selected table
def add_action(dropdown_var):
    connection = create_connection()
    cursor = connection.cursor()

    if dropdown_var.get() == "Students":
        query = """INSERT INTO students (school_id, full_name, course, year_level) 
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query)
        connection.commit()
        print("Student added successfully.")

    elif dropdown_var.get() == "Queue":
        queue_data = (1, "Queue 1", "Details 1", "Affiliation 1fdgfdgdgf", 100, "10:30", "No")
        query = """INSERT INTO queue (queue_number, queue_name, details, affiliation, ticket_number, time, completed) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, queue_data)
        connection.commit()
        print("Queue added successfully.")

    elif dropdown_var.get() == "Members":
        queue_data = (1, "Queue 1", "Details 1", "Affiliation 1fdgfdgdgf", 100, "10:30", "No")
        query = """INSERT INTO queue (queue_number, queue_name, details, affiliation, ticket_number, time, completed) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, queue_data)
        connection.commit()
        print("Queue added successfully.")

    elif dropdown_var.get() == "Passwords":
        queue_data = (1, "Queue 1", "Details 1", "Affiliation 1fdgfdgdgf", 100, "10:30", "No")
        query = """INSERT INTO queue (queue_number, queue_name, details, affiliation, ticket_number, time, completed) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, queue_data)
        connection.commit()
        print("Queue added successfully.")
    
    cursor.close()
    connection.close()
