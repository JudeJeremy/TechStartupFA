from tkinter import Tk, StringVar
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkCheckBox
from PIL import Image, ImageTk


# Initialize GUI
root = Tk()
root.title("Modern Login")
root.geometry("400x600")

# Style configuration
style = CTkFrame(root)
style.pack(expand=True, fill="both")
style.configure(corner_radius=20)
style.place(relx=0.5, rely=0.5, anchor="center")

# App icon
img = ImageTk.PhotoImage(Image.open("C:\Users\kusmandono.d\Downloads\app_icon.png").resize((100, 100)))
app_icon_label = CTkLabel(style, image=img)
app_icon_label.pack(pady=20)

# Login label
title_label = CTkLabel(style, text="Welcome Back!", font=("Roboto", 30))
title_label.pack(pady=20)

# Username entry
username_var = StringVar()
username_entry = CTkEntry(style, placeholder="Username", textvariable=username_var)
username_entry.pack(pady=10)

# Password entry
password_var = StringVar()
password_entry = CTkEntry(style, placeholder="Password", show="*", textvariable=password_var)
password_entry.pack(pady=10)

# Remember me checkbox
remember_me_var = BooleanVar()
remember_me = CTkCheckBox(style, text="Remember me", variable=remember_me_var)
remember_me.pack()

# Login button
login_button = CTkButton(style, text="Login", command=lambda: process_login(username_var.get(), password_var.get(), remember_me_var.get()))
login_button.pack(pady=20)

# Sign up button
signup_button = CTkButton(style, text="Sign Up", command=lambda: open_signup_page())
signup_button.pack(pady=10)


# Replace these functions with your actual login logic and signup page opening
def process_login(username, password, remember_me):
    print(f"Username: {username}, Password: {password}, Remember me: {remember_me}")
    # Implement your login logic here, e.g., check credentials, display error messages, etc.

def open_signup_page():
    print("Opening signup page")
    # Implement your signup page opening logic here


# Run the main loop
root.mainloop()
    
