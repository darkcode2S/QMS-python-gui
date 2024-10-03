import customtkinter as ctk
from PIL import Image

def satff_input_id(root):
    input_id_staff = ctk.CTkToplevel(root)
    input_id_staff.title("Input ID Staff")
    input_id_staff.iconbitmap("old-logo.ico")

    # Set appearance mode and color theme (Light/Dark modes)
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("dark-blue")

    # Center the window on the screen
    window_width = 800
    window_height = 600
    screen_width = input_id_staff.winfo_screenwidth()
    screen_height = input_id_staff.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    input_id_staff.geometry(f"{window_width}x{window_height}+{x}+{y}")

    main_frame = ctk.CTkFrame(input_id_staff, fg_color='transparent')
    main_frame.pack(expand=True)

    heading_label = ctk.CTkLabel(main_frame, text="PLEASE INSERT SCHOOL ID NUMBER",
                                        font=ctk.CTkFont(size=20, weight="bold"), 
                                        text_color="#000000", anchor="center")
    heading_label.pack(pady=(20,0), side='top')

    # Create the main frame for content
    frame = ctk.CTkFrame(main_frame, width=800, height=300, fg_color='#fff')
    frame.pack(expand=True, fill='both',pady=20, padx=230)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)

    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    frame.rowconfigure(4, weight=1)

    e1 = ctk.CTkEntry(frame, height=60)
    e1.grid(row=0, column=0, columnspan=3, sticky='wnes', pady=5, padx=5)

    b1 = ctk.CTkButton(frame, text='1',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b1.grid(row=1, column=0, sticky='wnes', pady=5, padx=5)
    b2 = ctk.CTkButton(frame, text='2',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b2.grid(row=1, column=1, sticky='wnes', pady=5, padx=5)
    b3 = ctk.CTkButton(frame, text='3',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b3.grid(row=1, column=2, sticky='wnes', pady=5, padx=5)

    b4 = ctk.CTkButton(frame, text='4',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b4.grid(row=2, column=0, sticky='wnes', pady=5, padx=5)
    b5 = ctk.CTkButton(frame, text='5',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b5.grid(row=2, column=1, sticky='wnes', pady=5, padx=5)
    b6 = ctk.CTkButton(frame, text='6',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b6.grid(row=2, column=2, sticky='wnes', pady=5, padx=5)

    b7 = ctk.CTkButton(frame, text='7',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b7.grid(row=3, column=0, sticky='wnes', pady=5, padx=5)
    b8 = ctk.CTkButton(frame, text='8',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b8.grid(row=3, column=1, sticky='wnes', pady=5, padx=5)
    b9 = ctk.CTkButton(frame, text='9',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b9.grid(row=3, column=2, sticky='wnes', pady=5, padx=5)

    delete_button = ctk.CTkButton(frame, text='Del', fg_color='#d68b26', text_color='#fff', border_width=1, border_color='#000', height=60)
    delete_button .grid(row=4, column=0, sticky='wnes', pady=5, padx=5)
    b0 = ctk.CTkButton(frame, text='0',fg_color='#fff', text_color='#000', border_width=1, border_color='#000', height=60)
    b0.grid(row=4, column=1, sticky='wnes', pady=5, padx=5)
    clear_button = ctk.CTkButton(frame, text='Clear', fg_color='#d68b26', text_color='#fff', border_width=1, border_color='#000', height=60)
    clear_button.grid(row=4, column=2, sticky='wnes', pady=5, padx=5)


    heading_label = ctk.CTkLabel(main_frame, text="Please proceed to create a ticket after entering your",
                                        text_color="#000000", anchor="center")
    heading_label.pack(padx=(0,20))

    heading_label = ctk.CTkLabel(main_frame, text="school ID number.",
                                        text_color="#000000", anchor="center")
    heading_label.pack(padx=(0,20))

    button_frame = ctk.CTkFrame(main_frame, fg_color='transparent')
    button_frame.pack(expand=True)

    cancel_button = ctk.CTkButton(button_frame, height=35, text='Cancel', fg_color='#fff', text_color='#000', border_width=1, border_color='#000',command=lambda:cancel())
    cancel_button.pack(side='left', pady=20, padx=20)

    create_ticket = ctk.CTkButton(button_frame, height=35, text='Create Ticket', fg_color='#fff', text_color='#000', border_width=1, border_color='#000')
    create_ticket.pack(side='left', padx=20)

    def cancel():
        input_id_staff.destroy()

    input_id_staff.grab_set()



