import customtkinter as ctk
from PIL import Image

class TransactionQueueApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Queue transaction")
        self.iconbitmap("old-logo.ico")

        # Set appearance mode and color theme (Light/Dark modes)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")

        # Center the window on the screen
        window_width = 800
        window_height = 440
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create the main frame for content
        self.create_main_frame()

    def create_main_frame(self):
        # Main frame
        frame = ctk.CTkFrame(self, width=700, height=300, fg_color="transparent")
        frame.pack(expand=True)

        # Load image using PIL and customtkinter
        photo = ctk.CTkImage(light_image=Image.open("old-logo.png"),
                             dark_image=Image.open("old-logo.png"),
                             size=(150, 150))

        # Create label for image
        image_label = ctk.CTkLabel(frame, image=photo, text="", anchor='center')
        image_label.pack(pady=(20, 20), side='left', padx=10)

        # Bold heading label
        heading_label = ctk.CTkLabel(frame, text="Welcome!",
                                     font=ctk.CTkFont(size=80, weight="bold"), 
                                     text_color="#000000", anchor="center")
        heading_label.pack(pady=(130, 0), padx=(0, 20))

        # Subheading label
        sub_label = ctk.CTkLabel(frame, text="Join the Entry Queue Here.",
                                 font=ctk.CTkFont(size=30, weight="bold"),
                                 text_color="#000000", anchor="center")
        sub_label.pack(pady=(0, 10))

        # Button frame
        button_frame = ctk.CTkFrame(frame, width=700, height=300, fg_color="transparent")
        button_frame.pack(expand=True, fill='x')

        # Proceed button
        proc_button = ctk.CTkButton(button_frame, text='Proceed', fg_color='#d68b26')
        proc_button.pack(pady=40, side="left", padx=20)
    

if __name__ == "__main__":
    app = TransactionQueueApp()
    app.mainloop()
