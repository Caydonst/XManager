import tkinter
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
import sqlite3
import bcrypt
from tkinter import messagebox

# Create "userdata.db" database and connect to it
conn = sqlite3.connect("userdata.db")
# Create "cursor" to execute sqlite commands - can call this anything
cursor = conn.cursor()

# Create "users" table if it doesn't already exist with username and password columns
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
)
""")

class App(customtkinter.CTk):

    def app_properties(self):
        # Set background image of window
        img1 = customtkinter.CTkImage(Image.open("bg5.jpg"), size=(1920, 1080))
        l1 = customtkinter.CTkLabel(master=app, image=img1)
        l1.pack()

        # Set window dimensions by pixels
        app.geometry("600x520")
        app.title("XManager")
        app.iconbitmap("logo.ico")

    # Display sign up window
    def signup_window(self):

        global username_entry1
        global password_entry1

        # Create a frame in app window
        frame1 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Create a label to display text
        signup_label = customtkinter.CTkLabel(master=frame1, text="Sign up", font=("Helvetica", 30, "bold"))
        signup_label.place(x=200, y=45)

        # Create entry box to type input
        username_entry1 = customtkinter.CTkEntry(master=frame1, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Username")
        username_entry1.place(x=120, y=110)

        password_entry1 = customtkinter.CTkEntry(master=frame1, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password", show="*")
        password_entry1.place(x=120, y=165)

        signup_label1 = customtkinter.CTkLabel(master=frame1, text="Already have an account?", font=("Arial", 12))
        signup_label1.place(x=200, y=195)

        # Create button to do something when pressed
        login_button1 = customtkinter.CTkButton(master=frame1, command=app.login_window, text="Login", font=("Arial", 12, "underline"), text_color="#4182d6", fg_color="#141414", hover_color="#141414", cursor="hand2", width=40)
        login_button1.place(x=340, y=195)

        signup_button1 = customtkinter.CTkButton(master=frame1, command=auth.signup, text="Sign up", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=260, height=50)
        signup_button1.place(x=120, y=240)

    # Display log in window
    def login_window(self):

        global frame2
        global username_entry2
        global password_entry2

        frame2 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
        frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        login_label = customtkinter.CTkLabel(master=frame2, text="Log in", font=("Helvetica", 30, "bold"))
        login_label.place(x=200, y=45)

        username_entry2 = customtkinter.CTkEntry(master=frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Username")
        username_entry2.place(x=120, y=110)

        password_entry2 = customtkinter.CTkEntry(master=frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password", show="*")
        password_entry2.place(x=120, y=165)

        signup_label1 = customtkinter.CTkLabel(master=frame2, text="Don't have an account?", font=("Arial", 12))
        signup_label1.place(x=200, y=195)

        login_button2 = customtkinter.CTkButton(master=frame2, command=app.signup_window, text="Sign up", font=("Arial", 12, "underline"), text_color="#4182d6", fg_color="#141414", hover_color="#141414",                                            cursor="hand2", width=40)
        login_button2.place(x=330, y=195)

        login_button3 = customtkinter.CTkButton(master=frame2, command=auth.login, text="Log in", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=260, height=50)
        login_button3.place(x=120, y=240)

    # Display frame when log in button is clicked
    def records_window(self):

        global check_var
        check_var = customtkinter.StringVar(value="off")

        global frame3

        frame3 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
        frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        add_button = customtkinter.CTkButton(master=frame3, command=app.create_record_window, text="+", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        add_button.place(x=440, y=20)

        edit_button = customtkinter.CTkButton(master=frame3, text="Edit", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        edit_button.place(x=440, y=80)

        delete_button = customtkinter.CTkButton(master=frame3, command=app.delete_login, text="Delete", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        delete_button.place(x=435, y=140)

        add_login_frame = customtkinter.CTkScrollableFrame(master=frame3, width=350, height=340, fg_color="#000000")
        add_login_frame.place(x=50, y=20)

        checkbox = customtkinter.CTkCheckBox(master=frame3, text="", bg_color="#000000", border_color="#424242", onvalue="on", offvalue="off", variable=check_var)
        checkbox.place(x=65, y=47)

        logout_button = customtkinter.CTkButton(master=frame3, command=app.logout, text="Logout", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        logout_button.place(x=435, y=330)

    # Display create record window
    def create_record_window(self):

        global name_entry1
        global password_entry3

        frame4 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3,
                                        border_color="#424242", corner_radius=0)
        frame4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        add_login_label = customtkinter.CTkLabel(master=frame4, text="Create Password Storage", font=("Helvetica", 30, "bold"))
        add_login_label.place(x=70, y=55)

        name_entry1 = customtkinter.CTkEntry(master=frame4, width=260, height=30, fg_color="#2a2a2a",
                                                 placeholder_text="Storage name")
        name_entry1.place(x=120, y=120)

        password_entry3 = customtkinter.CTkEntry(master=frame4, width=260, height=30, fg_color="#2a2a2a",
                                                 placeholder_text="Password")
        password_entry3.place(x=120, y=175)

        create_login_button3 = customtkinter.CTkButton(master=frame4, command=app.create_record_button, text="Create", fg_color="#294ec6",
                                                hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=150,
                                                height=30)
        create_login_button3.place(x=180, y=250)

        back_button3 = customtkinter.CTkButton(master=frame4, command=app.records_window, text="< Back", font=("Arial", 15), text_color="#4182d6", fg_color="#141414",
                                                hover_color="#141414", corner_radius=6, cursor="hand2", width=40,
                                                height=30)
        back_button3.place(x=20, y=20)

    # Display record window of record clicked
    def show_record_window(self):

        global frame5

        frame5 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3,
                                        border_color="#424242", corner_radius=0)
        frame5.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        show_record_label1 = customtkinter.CTkLabel(master=frame5, text=f"{name} Record",
                                                 font=("Helvetica", 30, "bold"))
        show_record_label1.place(x=140, y=55)

        show_record_label2 = customtkinter.CTkLabel(master=frame5, text="Password:", font=("Helvetica", 15, "bold"))
        show_record_label2.place(x=25, y=120)

        show_record_entry1 = customtkinter.CTkEntry(master=frame5, width=260, height=30, fg_color="#2a2a2a")
        show_record_entry1.place(x=120, y=120)

        back_button3 = customtkinter.CTkButton(master=frame5, command=app.raise3, text="< Back", font=("Arial", 15),
                                               text_color="#4182d6", fg_color="#141414",
                                               hover_color="#141414", corner_radius=6, cursor="hand2", width=40,
                                               height=30)
        back_button3.place(x=20, y=20)

        copy_button = customtkinter.CTkButton(master=frame5, command=lambda: app.copy(password), text="Copy",
                                              fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6,
                                              cursor="hand2", width=40, height=40)
        copy_button.place(x=400, y=115)

        show_record_entry1.insert(0, password)
        show_record_entry1.configure(state="disabled")

    # Display login window - "logout"
    def logout(self):

        app.login_window()

    # Creates a record from inputs
    def create_record_button(self):

        global name
        global password
        global storage_button
        name = name_entry1.get()
        password = password_entry3.get()
        # Take name and password entries and create record button to display record info when clicked
        storage_button = customtkinter.CTkButton(master=frame3, command=app.show_record_window, text=name, fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=300,
                                                height=50)
        storage_button.place(x=100, y=40)
        # Show that record has been created
        messagebox.showinfo("Success", "Password storage added.")
        frame3.tkraise()

    def show_password(self):

        app.show_record_window()

    # Deletes specified login
    def delete_login(self):

        # if check_var checkbox is checked
        if check_var.get() == "on":
            # Destroy record button
            storage_button.destroy()
            # Set checkbox to unchecked
            check_var.set("off")

    # Copy record password to clipboard
    def copy(self, password):
        # Clearing the clipboard
        app.clipboard_clear()
        # Copying record password to clipboard
        app.clipboard_append(password)
        # Create label to display that password has been copied
        copy_label = customtkinter.CTkLabel(master=frame5, text="Copied!", font=("Helvetica", 12), fg_color="#141414")
        copy_label.place(x=400, y=155)

    def raise3(self):
        frame3.tkraise()

class Authentication():

    # Storing user data into database
    def signup(self):

        username = username_entry1.get()
        password = password_entry1.get()
        if username != "" and password != "":
            cursor.execute("SELECT username FROM users WHERE username=?", [username])
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "Username already exists.")
            else:
                # Hashing the password
                encoded_password = password.encode("utf-8")
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                print(hashed_password)
                # Storing the username and hashed password into the database
                cursor.execute("INSERT INTO users VALUES (?, ?)", [username, hashed_password])
                conn.commit()
                messagebox.showinfo("Success", "Account has been created.")
        else:
            messagebox.showerror("Error", "Enter all data.")

    def login(self):

        username = username_entry2.get()
        password = password_entry2.get()
        if username != "" and password != "":
            # Fetching username and password from database
            cursor.execute("SELECT password FROM users WHERE username=?", [username])
            result = cursor.fetchone()
            if result:
                # Checking if username and password entered matches username and password in database
                if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                    app.records_window()
                else:
                    messagebox.showerror("Error", "Invalid login.")
            else:
                messagebox.showerror("Error", "Invalid login.")
        else:
            messagebox.showerror("Error", "Enter all data.")



if __name__ == "__main__":
    app = App()
    auth = Authentication()
    app.app_properties()
    app.login_window()
    app.mainloop()
