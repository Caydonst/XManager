import tkinter
import customtkinter
from PIL import Image
from CTkMessagebox import CTkMessagebox
import sqlite3
import bcrypt
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")

conn = sqlite3.connect("userdata.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL
)
""")

class App(customtkinter.CTk):

    master_key = "master"

    def signup_window(self):

        img1 = customtkinter.CTkImage(Image.open("bg5.jpg"), size=(1920, 1080))
        l1 = customtkinter.CTkLabel(master=start, image=img1)
        l1.pack()

        start.geometry("600x520")
        start.title("XManager")
        start.iconbitmap("logo.ico")

        global username_entry1
        global password_entry1

        frame1 = customtkinter.CTkFrame(master=start, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
        frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        signup_label = customtkinter.CTkLabel(master=frame1, text="Sign up", font=("Helvetica", 30, "bold"))
        signup_label.place(x=200, y=45)

        username_entry1 = customtkinter.CTkEntry(master=frame1, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Username")
        username_entry1.place(x=120, y=110)

        password_entry1 = customtkinter.CTkEntry(master=frame1, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password", show="*")
        password_entry1.place(x=120, y=165)

        signup_label1 = customtkinter.CTkLabel(master=frame1, text="Already have an account?", font=("Arial", 12))
        signup_label1.place(x=200, y=195)

        login_button1 = customtkinter.CTkButton(master=frame1, command=start.login_window, text="Login", font=("Arial", 12, "underline"), text_color="#4182d6", fg_color="#141414", hover_color="#141414", cursor="hand2", width=40)
        login_button1.place(x=340, y=195)

        signup_button1 = customtkinter.CTkButton(master=frame1, command=auth.signup, text="Sign up", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=260, height=50)
        signup_button1.place(x=120, y=240)

    def login_window(self):

        img1 = customtkinter.CTkImage(Image.open("bg5.jpg"), size=(1920, 1080))
        l1 = customtkinter.CTkLabel(master=start, image=img1)
        l1.pack()

        start.geometry("600x520")
        start.title("XManager")
        start.iconbitmap("logo.ico")

        global frame2
        global username_entry2
        global password_entry2

        frame2 = customtkinter.CTkFrame(master=start, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
        frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        login_label = customtkinter.CTkLabel(master=frame2, text="Log in", font=("Helvetica", 30, "bold"))
        login_label.place(x=200, y=45)

        username_entry2 = customtkinter.CTkEntry(master=frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Username")
        username_entry2.place(x=120, y=110)

        password_entry2 = customtkinter.CTkEntry(master=frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password", show="*")
        password_entry2.place(x=120, y=165)

        signup_label1 = customtkinter.CTkLabel(master=frame2, text="Don't have an account?", font=("Arial", 12))
        signup_label1.place(x=200, y=195)

        login_button2 = customtkinter.CTkButton(master=frame2, command=start.signup_window, text="Sign up", font=("Arial", 12, "underline"), text_color="#4182d6", fg_color="#141414", hover_color="#141414",                                            cursor="hand2", width=40)
        login_button2.place(x=330, y=195)

        login_button3 = customtkinter.CTkButton(master=frame2, command=auth.login, text="Log in", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=260, height=50)
        login_button3.place(x=120, y=240)

    def enter(self):

        img1 = customtkinter.CTkImage(Image.open("bg5.jpg"), size=(1920, 1080))
        l1 = customtkinter.CTkLabel(master=start, image=img1)
        l1.pack()

        start.geometry("600x520")
        start.title("XManager")
        start.iconbitmap("logo.ico")

        global check_var
        check_var = customtkinter.StringVar(value="off")

        global frame3

        frame3 = customtkinter.CTkFrame(master=start, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242")
        frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        add_button = customtkinter.CTkButton(master=frame3, command=start.create_login, text="+", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        add_button.place(x=440, y=20)

        edit_button = customtkinter.CTkButton(master=frame3, text="Edit", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        edit_button.place(x=440, y=80)

        delete_button = customtkinter.CTkButton(master=frame3, command=start.delete_login, text="Delete", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        delete_button.place(x=435, y=140)

        add_login_frame = customtkinter.CTkScrollableFrame(master=frame3, width=350, height=340, fg_color="#000000")
        add_login_frame.place(x=50, y=20)

        checkbox = customtkinter.CTkCheckBox(master=frame3, text="", bg_color="#000000", border_color="#424242", onvalue="on", offvalue="off", variable=check_var)
        checkbox.place(x=65, y=47)

        logout_button = customtkinter.CTkButton(master=frame3, command=start.logout, text="Logout", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
        logout_button.place(x=435, y=330)

    def create_login(self):

        global name_entry1
        global password_entry3

        frame4 = customtkinter.CTkFrame(master=start, width=500, height=400, fg_color="#141414", border_width=3,
                                        border_color="#424242")
        frame4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        add_login_label = customtkinter.CTkLabel(master=frame4, text="Create Password Storage", font=("Helvetica", 30, "bold"))
        add_login_label.place(x=70, y=55)

        name_entry1 = customtkinter.CTkEntry(master=frame4, width=260, height=30, fg_color="#2a2a2a",
                                                 placeholder_text="Storage name")
        name_entry1.place(x=120, y=120)

        password_entry3 = customtkinter.CTkEntry(master=frame4, width=260, height=30, fg_color="#2a2a2a",
                                                 placeholder_text="Password")
        password_entry3.place(x=120, y=175)

        create_login_button3 = customtkinter.CTkButton(master=frame4, command=start.create_login_button, text="Create", fg_color="#294ec6",
                                                hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=150,
                                                height=30)
        create_login_button3.place(x=180, y=250)

        back_button3 = customtkinter.CTkButton(master=frame4, command=start.enter, text="< Back", font=("Arial", 15), text_color="#4182d6", fg_color="#141414",
                                                hover_color="#141414", corner_radius=6, cursor="hand2", width=40,
                                                height=30)
        back_button3.place(x=20, y=20)

    def logout(self):
        start.login_window()

    def create_login_button(self):
        global name
        global password
        global storage_button
        name = name_entry1.get()
        password = password_entry3.get()
        storage_button = customtkinter.CTkButton(master=frame3, command=start.show_password, text=name, fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=300,
                                                height=50)
        storage_button.place(x=100, y=40)
        messagebox.showinfo("Success", "Password storage added.")
        frame3.tkraise()

    def show_password(self):
        get_password = customtkinter.CTkInputDialog(text="Enter Master Password", title="Master")
        if get_password.get_input() == start.master_key:
            CTkMessagebox(title=name, message=f"Password: {password}",
                      icon="check", option_1="Thanks")
        else:
            messagebox.showerror("Error", "Invalid master key.")

    def delete_login(self):
        if check_var.get() == "on":
            print("hello")
            storage_button.destroy()
            check_var.set("off")

class Authentication():

    def signup(self):
        username = username_entry1.get()
        password = password_entry1.get()
        if username != "" and password != "":
            cursor.execute("SELECT username FROM users WHERE username=?", [username])
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "Username already exists.")
            else:
                encoded_password = password.encode("utf-8")
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                print(hashed_password)
                cursor.execute("INSERT INTO users VALUES (?, ?)", [username, hashed_password])
                conn.commit()
                messagebox.showinfo("Success", "Account has been created")
        else:
            messagebox.showerror("Error", "Enter all data.")

    def login(self):
        username = username_entry2.get()
        password = password_entry2.get()
        if username != "" and password != "":
            cursor.execute("SELECT password FROM users WHERE username=?", [username])
            result = cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                    start.enter()
                else:
                    messagebox.showerror("Error", "Invalid login")
            else:
                messagebox.showerror("Error", "Invalid login")
        else:
            messagebox.showerror("Error", "Enter all data.")

        img1 = customtkinter.CTkImage(Image.open("bg5.jpg"), size=(1920, 1080))
        l1 = customtkinter.CTkLabel(master=start, image=img1)
        l1.pack()



if __name__ == "__main__":
    start = App()
    auth = Authentication()
    start.login_window()
    start.mainloop()
