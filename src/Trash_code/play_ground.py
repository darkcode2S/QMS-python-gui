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

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=3, column=4, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=4, column=4, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
