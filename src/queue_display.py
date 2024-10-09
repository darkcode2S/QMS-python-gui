import customtkinter as ctk
from PIL import Image
from db import create_connection

q_display = ctk.CTk()
q_display.title("Queue display")
q_display.iconbitmap("old-logo.ico")

# Set the window to fullscreen
q_display.attributes("-fullscreen", True)

# Exit fullscreen with the Escape key
def exit_fullscreen(event):
    q_display.attributes("-fullscreen", False)

# Bind the Escape key to exit fullscreen
q_display.bind("<Escape>", exit_fullscreen)

# Set appearance mode and color theme (Light/Dark modes)
ctk.set_appearance_mode("darkgray")
ctk.set_default_color_theme("dark-blue")

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

#navbar label----------------------------------------------------------------------------------------
window_label = ctk.CTkLabel(q_display,
                            text='WINDOW',
                            fg_color='lightblue',
                            # anchor='s',
                            # compound='left', 
                            text_color='#000',
                            font=ctk.CTkFont(size=50, weight="bold"))
window_label.grid(row=0, column=0, sticky='news')

prep_label = ctk.CTkLabel(q_display,
                            text='PREPARING',
                            fg_color='lightblue',
                            # anchor='w',
                            # compound='left', 
                            text_color='#000',
                            font=ctk.CTkFont(size=50, weight="bold"))
prep_label.grid(row=0, column=1, sticky='news')

serving_label = ctk.CTkLabel(q_display,
                            text='SERVING',
                            fg_color='lightblue',
                            # anchor='w',
                            # compound='left', 
                            text_color='#000',
                            font=ctk.CTkFont(size=50, weight="bold"))
serving_label.grid(row=0, column=2, sticky='news')

#sidebar label----------------------------------------------------------------------------------------------
cashier_label = ctk.CTkLabel(q_display,
                            text='CASHIER',
                            # fg_color='#a45e14',
                            fg_color='lightgray',
                            text_color='#000',
                            font=ctk.CTkFont(size=30, weight="bold"))
cashier_label.grid(row=1, column=0, sticky='news', pady=3, padx=3)

scholarship_label = ctk.CTkLabel(q_display,
                            text='SCHOLARSHIP \nCOORDINATOR',
                            # fg_color='#a45e14',
                            fg_color='lightgray',
                            text_color='#000',
                            font=ctk.CTkFont(size=30, weight="bold"))
scholarship_label.grid(row=2, column=0, sticky='news', pady=3, padx=3)

promisorry_label = ctk.CTkLabel(q_display,
                            text='PROMISORRY NOTE \nCOORDINATOR',
                            # fg_color='#a45e14',
                            fg_color='lightgray',
                            text_color='#000',
                            font=ctk.CTkFont(size=30, weight="bold"))
promisorry_label.grid(row=3, column=0, sticky='news', pady=3, padx=3)

#Preparing queue number------------------------------------------------------------------------------------------------
conn = create_connection()                            
cursor = conn.cursor()

query = "SELECT queue_num FROM queue_display LIMIT 1 OFFSET 1"
cursor.execute(query)
get_snum = cursor.fetchone()

# Set the default value to 0 if no result is found
if get_snum is None:
    get_snum = 0
else:
    get_snum = get_snum[0]  # fetchone returns a tuple, get the first value

p_c_number = ctk.CTkLabel(q_display,
                          text=str(get_snum),  # Convert the number to string
                          fg_color='red',
                          text_color='#000',
                          font=ctk.CTkFont(size=80, weight="bold"))
p_c_number.grid(row=1, column=1, sticky='news', pady=3, padx=3)

p_sc_number = ctk.CTkLabel(q_display,
                            text='01',
                            fg_color='red',
                            # anchor='w',
                            # compound='left', 
                            text_color='#000',
                            font=ctk.CTkFont(size=80, weight="bold"))
p_sc_number.grid(row=2, column=1, sticky='news', pady=3, padx=3)

p_pnc_number = ctk.CTkLabel(q_display,
                            text='168',
                            fg_color='red',
                            # anchor='w',
                            # compound='left', 
                            text_color='#000',
                            font=ctk.CTkFont(size=80, weight="bold"))
p_pnc_number.grid(row=3, column=1, sticky='news', pady=3, padx=3)

#Serving queue number-----------------------------------------------------------------------------------------
conn = create_connection()                            
cursor = conn.cursor()

query = "SELECT queue_num FROM queue_display"
cursor.execute(query)
get_num = cursor.fetchone()

# Set the default value to 0 if no result is found
if get_num is None:
    get_num = 0
else:
    get_num = get_num[0]  # fetchone returns a tuple, get the first value

s_c_number = ctk.CTkLabel(q_display,
                          text=str(get_num),  # Convert the number to string
                          fg_color='yellow',
                          text_color='#000',
                          font=ctk.CTkFont(size=80, weight="bold"))
s_c_number.grid(row=1, column=2, sticky='news', pady=3, padx=3)

s_sc_number = ctk.CTkLabel(q_display,
                            text='69',
                            fg_color='yellow',
                            # anchor='w',
                            # compound='left', 
                            text_color='#000',
                            font=ctk.CTkFont(size=80, weight="bold"))
s_sc_number.grid(row=2, column=2, sticky='news', pady=3, padx=3)

s_pnc_number = ctk.CTkLabel(q_display,
                            text='103',
                            fg_color='yellow',
                            # anchor='w',
                            # compound='left', 
                            text_color='#000',
                            font=ctk.CTkFont(size=80, weight="bold"))
s_pnc_number.grid(row=3, column=2, sticky='news', pady=3, padx=3)


# Function to expose these widgets
def get_widgets():
    return p_c_number, s_c_number


q_display.mainloop()


