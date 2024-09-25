import customtkinter as ctk
from tkinter import ttk


#QUEUE TABLE FUNCTION++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def queue_table(table):
    table['columns'] = ('Queue number', 'School ID', 'Full name', 'Transaction', 'Affiliation',
                         'Phone', 'Compilation time', 'Voided')
    
    table.column("#0", width=0, stretch="no")  # Hide the first column
    table.column("Queue number", anchor="center", width=80)  # Lowercase 'n' to match the columns definition
    table.column("School ID", anchor="center", width=80)
    table.column("Full name", anchor="center", width=80)
    table.column("Transaction", anchor="center", width=80)
    table.column("Affiliation", anchor="center", width=80)
    table.column("Phone", anchor="center", width=80)
    table.column("Compilation time", anchor="center", width=80)  # Ensure same column name
    table.column("Voided", anchor="center", width=80)

    table.heading("#0", text="")
    table.heading("Queue number", text="Queue Number")  # Use correct name for heading too
    table.heading("School ID", text="School ID")
    table.heading("Full name", text="Full name")
    table.heading("Transaction", text="Transaction")
    table.heading("Affiliation", text="Affiliation")
    table.heading("Phone", text="Phone")
    table.heading("Compilation time", text="Compilation Time")
    table.heading("Voided", text="Voided")


#MEMBER TABLE FUNCTION
def member_table(table):
    table['columns'] = ('ID', 'Name', 'Details')
    table.column("#0", width=0, stretch="no")  # Hide the first column
    table.column("ID", anchor="center", width=80)
    table.column("Name", anchor="w", width=120)
    table.column("Details", anchor="w", width=300)
    table.heading("#0", text="", anchor="center")
    table.heading("ID", text="ID", anchor="center")
    table.heading("Name", text="Name", anchor="w")
    table.heading("Details", text="Details", anchor="w")



def password_table(table):
    table['columns'] = ('School ID','Full name','Affiliation', 'Username', 'Password')
    table.column("#0", width=0, stretch="no")  # Hide the first column
    table.column("School ID", anchor="center", width=80)
    table.column("Full name", anchor="center", width=80)
    table.column("Affiliation", anchor="center", width=80)
    table.column("Username", anchor="center", width=80)
    table.column("Password", anchor="center", width=80)
    
    table.heading("#0", text="", anchor="center")
    table.heading("School ID", text="School ID")
    table.heading("Full name", text="Full name")
    table.heading("Affiliation", text="Affiliation")
    table.heading("Username", text="Username")
    table.heading("Password", text="Password")


