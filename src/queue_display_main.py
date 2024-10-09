import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image
from db import create_connection

# Initialize the queue display window with ttkbootstrap
q_display = ttk.Window(themename="superhero")  # 'superhero' theme for a modern dark design
q_display.title("Queue display")
q_display.iconbitmap("old-logo.ico")

# Set the window to fullscreen
q_display.attributes("-fullscreen", True)

# Exit fullscreen with the Escape key
def exit_fullscreen(event):
    q_display.attributes("-fullscreen", False)

q_display.bind("<Escape>", exit_fullscreen)

# Center the window on the screen
window_width = 900
window_height = 500
screen_width = q_display.winfo_screenwidth()
screen_height = q_display.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
q_display.geometry(f"{window_width}x{window_height}+{x}+{y}")

q_display.columnconfigure(0, weight=1)
q_display.columnconfigure(1, weight=1)
q_display.columnconfigure(2, weight=1)

q_display.rowconfigure(0, weight=1)
q_display.rowconfigure(1, weight=1)
q_display.rowconfigure(2, weight=1)
q_display.rowconfigure(3, weight=1)

# Header labels with modern design
window_label = ttk.Label(q_display,
                         text='WINDOW',
                         bootstyle="info",
                         anchor='center',
                         font=('Helvetica', 48, 'bold'))
window_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

prep_label = ttk.Label(q_display,
                       text='PREPARING',
                       bootstyle="info",
                       anchor='center',
                       font=('Helvetica', 48, 'bold'))
prep_label.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

serving_label = ttk.Label(q_display,
                          text='SERVING',
                          bootstyle="info",
                          anchor='center',
                          font=('Helvetica', 48, 'bold'))
serving_label.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

# Sidebar labels with modern design
cashier_label = ttk.Label(q_display,
                          text='CASHIER',
                          bootstyle="secondary",
                          anchor='center',
                          font=('Helvetica', 32, 'bold'))
cashier_label.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

scholarship_label = ttk.Label(q_display,
                              text='SCHOLARSHIP\nCOORDINATOR',
                              bootstyle="secondary",
                              anchor='center',
                              font=('Helvetica', 32, 'bold'))
scholarship_label.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

promissory_label = ttk.Label(q_display,
                             text='PROMISSORY \nNOTE\nCOORDINATOR',
                             bootstyle="secondary",
                             anchor='center',
                             font=('Helvetica', 32, 'bold'))
promissory_label.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)

# Preparing queue number------------------------------------------------------------------------------------
conn = create_connection()
cursor = conn.cursor()

query = "SELECT queue_num FROM queue_display LIMIT 1 OFFSET 1"
cursor.execute(query)
get_snum = cursor.fetchone()

# Set the default value to 0 if no result is found
get_snum = get_snum[0] if get_snum else 0

cursor.fetchall()

query_pnc_prep = "SELECT promisorry_number FROM queue_display_promisorry LIMIT 1 OFFSET 1"
cursor.execute(query_pnc_prep)
get_num_pnc_prep = cursor.fetchone()

# Set the default value to 0 if no result is found
get_num_pnc_prep = get_num_pnc_prep[0] if get_num_pnc_prep else 0

cursor.fetchall()

query_sc_prep = "SELECT queue_sc FROM queue_display_sc LIMIT 1 OFFSET 1"
cursor.execute(query_sc_prep)
get_num_sc_prep = cursor.fetchone()

# Set the default value to 0 if no result is found
get_num_sc_prep = get_num_sc_prep[0] if get_num_sc_prep else 0

p_c_number = ttk.Label(q_display,
                       text=str(get_snum),
                       bootstyle="danger",
                       anchor='center',
                       font=('Helvetica', 80, 'bold'))
p_c_number.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

p_sc_number = ttk.Label(q_display,
                        text=str(get_num_sc_prep),
                        bootstyle="danger",
                        anchor='center',
                        font=('Helvetica', 80, 'bold'))
p_sc_number.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)

p_pnc_number = ttk.Label(q_display,
                         text=str(get_num_pnc_prep),
                         bootstyle="danger",
                         anchor='center',
                         font=('Helvetica', 80, 'bold'))
p_pnc_number.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

# Serving queue number--------------------------------------------------------------------------------
# First query: Fetch queue number for the first label
query = "SELECT queue_num FROM queue_display"
cursor.execute(query)
get_num = cursor.fetchone()

# Set the default value to 0 if no result is found
get_num = get_num[0] if get_num else 0

# After fetching the result, use fetchall() or reset the cursor
cursor.fetchall()  # This ensures all rows are processed (even if no more rows are there)

# Second query: Fetch promisorry number for the second label
query_pnc_serve = "SELECT promisorry_number FROM queue_display_promisorry"
cursor.execute(query_pnc_serve)
get_num_pnc_serve = cursor.fetchone()

# Set the default value to 0 if no result is found
get_num_pnc_serve = get_num_pnc_serve[0] if get_num_pnc_serve else 0

cursor.fetchall() 

query_sc_serve = "SELECT queue_sc FROM queue_display_sc"
cursor.execute(query_sc_serve)
get_num_sc_serve = cursor.fetchone()

# Set the default value to 0 if no result is found
get_num_sc_serve = get_num_sc_serve[0] if get_num_sc_serve else 0

# Now proceed with the labels
s_c_number = ttk.Label(q_display,
                       text=str(get_num),
                       bootstyle="warning",
                       anchor='center',
                       font=('Helvetica', 80, 'bold'))
s_c_number.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)

s_sc_number = ttk.Label(q_display,
                        text=str(get_num_sc_serve),
                        bootstyle="warning",
                        anchor='center',
                        font=('Helvetica', 80, 'bold'))
s_sc_number.grid(row=2, column=2, sticky='nsew', padx=10, pady=10)

s_pnc_number = ttk.Label(q_display,
                         text=str(get_num_pnc_serve),
                         bootstyle="warning",
                         anchor='center',
                         font=('Helvetica', 80, 'bold'))
s_pnc_number.grid(row=3, column=2, sticky='nsew', padx=10, pady=10)


q_display.mainloop()
