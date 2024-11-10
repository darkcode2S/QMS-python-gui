import tkinter as tk
from tkinter import font
from datetime import datetime

from center_window import center_window


    # Initialize the main window
root = tk.Tk()
root.title("View Queue Ticket")
center_window(800, 600, root)
root.configure(bg="#D3D3D3")  # Light gray background for the window

    # Custom font for larger text
large_font = font.Font(family="Helvetica", size=48, weight="bold")
title_font = font.Font(family="Helvetica", size=30, weight="bold")
medium_font = font.Font(family="Helvetica", size=15)
small_font = font.Font(family="Helvetica", size=10)

# Title Label
title_label = tk.Label(root, text="VIEW QUEUE TICKET", font=title_font, bg="#D3D3D3")
title_label.pack(pady=10)

    # Frame for ticket information
ticket_frame = tk.Frame(root, bg="white", padx=20, pady=20)
ticket_frame.pack(pady=10)

    # Get current date in MM-DD-YY format
current_date = datetime.now().strftime("%m-%d-%y")

    # Ticket Number
queue_label = tk.Label(ticket_frame, text="YOUR QUEUE NUMBER:", font=small_font, fg="black", bg="white")
queue_label.pack()

queue_label = tk.Label(ticket_frame, text="01", font=large_font, fg="black", bg="white")
queue_label.pack()

queue_label = tk.Label(ticket_frame, text="WINDOW:", font=small_font, fg="black", bg="white")
queue_label.pack()

    # Counter Information
counter_label = tk.Label(ticket_frame, text="C1", font=large_font, fg="black", bg="white")
counter_label.pack()

queue_label = tk.Label(ticket_frame, text="PLEASE BE SEATED.\n YOU WILL BE SERVED SHORTLY.", font=small_font, fg="black", bg="white")
queue_label.pack()

queue_label = tk.Label(ticket_frame, text=current_date, font=small_font, fg="black", bg="white")
queue_label.pack(pady=(20,10), anchor="e")

    # Instructional Text
instruction_label = tk.Label(root, text="Click Print Ticket to generate your queue ticket.\n"
                                            "Thank you for your submission! We appreciate your feedback. if you have any\n further inquiries or concerns, please don't hesitate to reach out to us.",
                                font=small_font, bg="#D3D3D3")
instruction_label.pack(pady=10)

    # Next Ticket Button
next_button = tk.Button(root, text="Next Ticket", font=medium_font)
next_button.pack(pady=10)

    # Run the Tkinter event loop
root.mainloop()
