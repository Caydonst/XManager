import tkinter
import customtkinter
from PIL import Image
import tkinter
from CTkMessagebox import CTkMessagebox
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

font1 = ("Helvetica", 25, "bold")
font2 = ("Arial", 17, "bold")
font3 = ("Arial", 13, "bold")
font4 = ("Arial", 13, "bold", "underline")

X = 150
Y = 150

img1 = customtkinter.CTkImage(Image.open("bg5.jpg"), size=(1920, 1080))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

#img1 = customtkinter.CTkImage(Image.open("pattern.png"))
#l1 = customtkinter.CTkFrame(master=app, image=img1)
#l1.pack()

frame1 = customtkinter.CTkFrame(master=app, width=320, height=360, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
frame2 = customtkinter.CTkFrame(master=app, width=320, height=360, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
frame3 = customtkinter.CTkFrame(master=app, width=420, height=580, fg_color="#000000", border_width=3, border_color="#424242")

def signup():

    app.geometry("600x520")
    app.title("XManager")
    app.iconbitmap("logo.ico")

    frame1 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
    frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    signup_label = customtkinter.CTkLabel(master=frame1, text="Sign up", font=("Helvetica", 30, "bold"))
    signup_label.place(x=200, y=45)

    username_entry1 = customtkinter.CTkEntry(master=frame1, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Username")
    username_entry1.place(x=120, y=110)

    password_entry1 = customtkinter.CTkEntry(master=frame1, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password")
    password_entry1.place(x=120, y=165)

    signup_label1 = customtkinter.CTkLabel(master=frame1, text="Already have an account?", font=("Arial", 12))
    signup_label1.place(x=200, y=195)

    login_button1 = customtkinter.CTkButton(master=frame1, command=login, text="Login", font=("Arial", 12, "underline"), text_color="#4182d6", fg_color="#141414", hover_color="#141414", cursor="hand2", width=40)
    login_button1.place(x=340, y=195)

    login_button2 = customtkinter.CTkButton(master=frame1, command=enter, text="Sign up", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=260, height=50)
    login_button2.place(x=120, y=240)


def login():

    #clear_widgets(frame3)
    #clear_widgets(frame1)

    app.geometry("600x520")
    app.title("XManager")
    app.iconbitmap("logo.ico")

    frame2 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3, border_color="#424242", corner_radius=0)
    frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    login_label = customtkinter.CTkLabel(master=frame2, text="Log in", font=("Helvetica", 30, "bold"))
    login_label.place(x=200, y=45)

    username_entry1 = customtkinter.CTkEntry(master=frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Username")
    username_entry1.place(x=120, y=110)

    password_entry1 = customtkinter.CTkEntry(master=frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password", show="*")
    password_entry1.place(x=120, y=165)

    signup_label1 = customtkinter.CTkLabel(master=frame2, text="Don't have an account?", font=("Arial", 12))
    signup_label1.place(x=200, y=195)

    login_button1 = customtkinter.CTkButton(master=frame2, command=signup, text="Sign up", font=("Arial", 12, "underline"), text_color="#4182d6", fg_color="#141414", hover_color="#141414",                                            cursor="hand2", width=40)
    login_button1.place(x=330, y=195)

    login_button = customtkinter.CTkButton(master=frame2, command=enter, text="Log in", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=260, height=50)
    login_button.place(x=120, y=240)

def enter():

    #clear_widgets(frame1)
    #clear_widgets(frame2)

    app.geometry("600x520")
    app.title("XManager")
    app.iconbitmap("logo.ico")

    frame3 = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#000000", border_width=3, border_color="#424242")
    frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    add_button = customtkinter.CTkButton(master=frame3, command=open, text="+", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
    add_button.place(x=440, y=20)

    edit_button = customtkinter.CTkButton(master=frame3, text="Edit", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
    edit_button.place(x=440, y=80)

    delete_button = customtkinter.CTkButton(master=frame3, text="Delete", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
    delete_button.place(x=435, y=140)

    add_login_frame = customtkinter.CTkScrollableFrame(master=frame3, width=350, height=340, fg_color="#141414")
    add_login_frame.place(x=50, y=20)

    checkbox = customtkinter.CTkCheckBox(master=frame3, text="", bg_color="#141414", border_color="#424242")
    checkbox.place(x=65, y=47)

    logout_button = customtkinter.CTkButton(master=frame3, command=logout, text="Logout", fg_color="#294ec6", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=40, height=40)
    logout_button.place(x=435, y=330)

    add_login_button = customtkinter.CTkButton(master=frame3, text="First Login", fg_color="#294ec6", bg_color="#141414", hover_color="#1e3a96", corner_radius=6, cursor="hand2", width=300, height=40)
    add_login_button.place(x=100, y=40)


def logout():

    #clear_widgets(frame3)
    login()

def clear_widgets(frame1):
    for widget in frame1.winfo_children():
        widget.destroy()


def open():
    dialog = customtkinter.CTkInputDialog(text="Enter name:", title="Username")
    global name
    name = dialog.get_input()
    global name1
    dialog2 = customtkinter.CTkInputDialog(text="Enter password:", title="Password")
    name1 = dialog2.get_input()
    add_login_button2 = customtkinter.CTkButton(master=app, command=login_name, text=name, fg_color="#294ec6",
                                               bg_color="#141414", hover_color="#1e3a96", corner_radius=6,
                                               cursor="hand2", width=300, height=40)
    add_login_button2.place(x=150, y=150)

def login_name():
    CTkMessagebox(title=name, message=f"Password: {name1}",
                  icon="check", option_1="Thanks")



signup()
app.mainloop()
