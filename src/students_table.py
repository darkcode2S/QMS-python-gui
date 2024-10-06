import customtkinter as ctk
import tkinter as tk
from PIL import Image


class CounterStaffApp:
    def __init__(self):
        self.counter_staff = ctk.CTk()
        self.setup_window()
        self.setup_frames()
        self.setup_content()
        self.counter_staff.mainloop()

    def setup_window(self):
        self.counter_staff.title("Counter Staff")
        self.counter_staff.iconbitmap("old-logo.ico")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
        self.center_window(800, 440)

    def center_window(self, width, height):
        screen_width = self.counter_staff.winfo_screenwidth()
        screen_height = self.counter_staff.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.counter_staff.geometry(f"{width}x{height}+{x}+{y}")

    def setup_frames(self):
        self.counter_staff.columnconfigure(0, weight=1)
        self.counter_staff.columnconfigure(1, weight=1)
        self.left_frame = self.create_frame(0)
        self.right_frame = self.create_frame(1, fg_color='transparent')

    def create_frame(self, column, **kwargs):
        frame = ctk.CTkFrame(self.counter_staff, **kwargs)
        frame.grid(row=0, column=column, sticky='news')
        return frame

    def setup_content(self):
        self.setup_image_label()
        self.setup_right_content()

    def setup_image_label(self):
        self.original_image = Image.open("building1.jpg")
        self.image_label = ctk.CTkLabel(self.left_frame, text="")
        self.image_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.left_frame.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        new_width = self.left_frame.winfo_width()
        new_height = self.left_frame.winfo_height()
        resized_image = self.original_image.resize((new_width, new_height))
        new_ctk_image = ctk.CTkImage(light_image=resized_image, size=(new_width, new_height))
        self.image_label.configure(image=new_ctk_image)
        self.image_label.image = new_ctk_image

    def setup_right_content(self):
        content_frame = ctk.CTkFrame(self.right_frame, fg_color='transparent')
        content_frame.pack(expand=True)

        title_label = ctk.CTkLabel(content_frame, text='Welcome back!', font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(pady=20, padx=20)

        name_label = ctk.CTkLabel(content_frame, text='John Doe', font=ctk.CTkFont(size=20, weight="bold"))
        name_label.pack(pady=(20, 0), padx=20)

        # Continue setting up other UI elements...

    def stand_by(self):
        self.counter_staff.destroy()

# Start the application
if __name__ == "__main__":
    CounterStaffApp()
