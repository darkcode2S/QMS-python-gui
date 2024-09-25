import customtkinter as ctk

# Custom class that contains a CTkTabview
class CustomTabViewApp(ctk.CTk):
    def __init__(self, table_frame):
        super().__init__()
              
        # Create and add the tabview to the left of the frame
        self.tab_view = ctk.CTkTabview(table_frame, width=500, height=300, fg_color="lightblue")
        self.tab_view.add("BSCS")   # Add the BSCS tab
        self.tab_view.add("CRIM")   # Add the CRIM tab
        self.tab_view.add("NURSE")  # Add the NURSE tab
        self.tab_view.pack(fill="both", padx=10, pady=10)
        
        # Add some content (buttons) to each tab
        self.add_tab_content()

    def add_tab_content(self):
        # Add buttons to the "BSCS" tab
        tab_button = ctk.CTkButton(master=self.tab_view.tab("BSCS"), text="BSCS Button")
        tab_button.pack(padx=20, pady=10)
        
        # Add buttons to the "CRIM" tab
        tab_button = ctk.CTkButton(master=self.tab_view.tab("CRIM"), text="CRIM Button")
        tab_button.pack(padx=20, pady=10)
        
        # Add buttons to the "NURSE" tab
        tab_button = ctk.CTkButton(master=self.tab_view.tab("NURSE"), text="NURSE Button")
        tab_button.pack(padx=20, pady=10)


# # Run the application
# if __name__ == "__main__":
#     app = CustomTabViewApp()
#     app.mainloop()
