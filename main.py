import tkinter
import customtkinter
from PIL import Image, ImageDraw
import sqlite3
import bcrypt
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import random
import numpy as np
import os

# Create "userdata.db" database and connect to it
conn = sqlite3.connect("userdata.db")
# Create "cursor" to execute sqlite commands - can call this anything
cursor = conn.cursor()

# Create "users" table if it doesn't already exist with username and password columns
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password  TEXT NOT NULL,
        profile_icon TEXT NOT NULL
)
""")

# Importing all the images, so they can be used in the code
edit_icon = customtkinter.CTkImage(Image.open("images/edit_icon1.png"), size=(25, 25))
edit_icon2 = customtkinter.CTkImage(Image.open("images/edit_icon2.png"), size=(25, 25))
add_icon = customtkinter.CTkImage(Image.open("images/add_icon2.png"), size=(35, 35))
copy_icon = customtkinter.CTkImage(Image.open("images/copy_icon1.png"), size=(25, 25))
logout_icon = customtkinter.CTkImage(Image.open("images/logout_icon2.png"), size=(30, 30))
delete_icon = customtkinter.CTkImage(Image.open("images/delete_icon1.png"), size=(25, 25))
logo_icon = customtkinter.CTkImage(Image.open("images/logo.ico"), size=(60, 60))
profile_icon = customtkinter.CTkImage(Image.open("images/profile_icon1.png"), size=(180, 180))
back_icon = customtkinter.CTkImage(Image.open("images/back_icon.png"), size=(25, 25))
lock_icon = customtkinter.CTkImage(Image.open("images/lock_icon2.png"), size=(25, 25))
key_icon = customtkinter.CTkImage(Image.open("images/key_icon3.png"), size=(40, 40))
profile_icon2 = customtkinter.CTkImage(Image.open("images/profile_icon6.png"), size=(35, 35))
photo_icon = customtkinter.CTkImage(Image.open("images/photo_icon3.png"), size=(25, 25))
random_icon = customtkinter.CTkImage(Image.open("images/random_icon3.png"), size=(28, 30))
user_icon = customtkinter.CTkImage(Image.open("images/user_icon2.png"), size=(25, 25))
add_user_icon = customtkinter.CTkImage(Image.open("images/add_user_icon4.png"), size=(25, 25))
user_icon2 = customtkinter.CTkImage(Image.open("images/user_icon4.png"), size=(80, 80))
enter_icon = customtkinter.CTkImage(Image.open("images/enter_icon.png"), size=(25, 25))
save_icon = customtkinter.CTkImage(Image.open("images/save_icon.png"), size=(25, 25))



class App(customtkinter.CTk):

    global sidebar_frame

    # Window properties
    def app_properties(self):

        # Set window dimensions by pixels
        app.geometry("600x520")
        # Set app title
        app.title("XManager")
        # Set app icon
        app.iconbitmap("images/logo.ico")
        # Set app dimensions in a grid layout
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=1)


    def welcome_window(self):

        # Creating frame that will cover the entire app bc dimensions are the same as the app.geometry above.
        # Corner radius is what will round out the corners, since it is 0 it will just be a 90-degree angle.
        # The grid function is how we place the frame. row and column means the top left corner of the frame will be in row 0, column 0 like a grid.
        # Columnspan means that the frame will stretch across 2 columns, which is the entire window since the whole window is only 2 columns
        # Sticky means the frame will stick to the edges of the app no matter what dimensions the window is in. "nesw" are the cardinal directions, so the frame will stick to all edges of the window.

        global button_name3
        global button

        welcome_frame = customtkinter.CTkFrame(master=app, width=600, height=520, fg_color="#141414", corner_radius=0)
        welcome_frame.grid(row=0, column=0, columnspan=2, sticky="nesw")

        welcome_frame2 = customtkinter.CTkFrame(master=app, fg_color="#242424")
        welcome_frame2.grid(row=0, column=0, columnspan=2, sticky="new")

        # Place function has multiple uses. You can either use pixels to place the widget, or you can use relx, rely, anchor.
        # relx and rely are much better because you can center widgets very easily. ie. (relx=0.5, rely=0.5, anchor=tkinter.CENTER) centers the widget in the frame.
        welcome_frame3 = customtkinter.CTkFrame(master=welcome_frame, width=400, height=320, fg_color="#141414")
        welcome_frame3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        welcome_frame4 = customtkinter.CTkFrame(master=welcome_frame, width=200, height=40, fg_color="#141414")
        welcome_frame4.place(relx=0.5, rely=0.79, anchor=tkinter.CENTER)

        icon_label = customtkinter.CTkLabel(master=welcome_frame2, text="", image=logo_icon, bg_color="#242424")
        icon_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")

        welcome_label = customtkinter.CTkLabel(master=welcome_frame3, text="", font=("Helvetica", 30, "bold"), bg_color="#141414", image=user_icon2)
        welcome_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        xmanager_label = customtkinter.CTkLabel(master=welcome_frame2, text="XManager", font=("Helvetica", 40, "bold"),
                                               bg_color="#242424")
        xmanager_label.grid(row=1, column=2, sticky="w")

        accounts_frame = customtkinter.CTkScrollableFrame(master=welcome_frame3, width=180, height=200,
                                                           fg_color="#0A0A0A", bg_color="#141414", corner_radius=5)
        accounts_frame.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

        # pack is good to use if you want equal distance between widgets. padx and pady adds that amount of pixels of padding around the widget
        # It's nice when adding widgets using a loop so that each widget has equal spacing and they don't end up on top of eachother.
        # An example of this is is at the bottom of the function, I'm using a for loop and the pack() function to create buttons and display them with 0 pixels of padding.

        signup_button = customtkinter.CTkButton(master=app, command=app.signup_window, text="Sign up", font=("Helvetica", 20), text_color="#294ec6", fg_color="#141414",
                                                hover_color="#242424", corner_radius=0, cursor="hand2", width=200,
                                                height=80, bg_color="#141414")
        signup_button.grid(row=0, column=0, columnspan=2, sticky="sew")

        #horizontal_divider_frame = customtkinter.CTkFrame(master=welcome_frame4, width=50, height=2, fg_color="#424242", corner_radius=0)
        #horizontal_divider_frame.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

        #horizontal_divider_frame2 = customtkinter.CTkFrame(master=welcome_frame4, width=500, height=2, fg_color="#424242",
        #                                                  corner_radius=0)
        #horizontal_divider_frame2.place(relx=0.2, rely=0.95, anchor=tkinter.CENTER)

        vertical_divider_frame = customtkinter.CTkFrame(master=welcome_frame3, width=2, height=300, fg_color="#424242",
                                               corner_radius=0)
        vertical_divider_frame.place(relx=0.05, rely=0.5, anchor=tkinter.CENTER)

        vertical_divider_frame2 = customtkinter.CTkFrame(master=welcome_frame3, width=2, height=300, fg_color="#424242",
                                                        corner_radius=0)
        vertical_divider_frame2.place(relx=0.95, rely=0.5, anchor=tkinter.CENTER)

        #or_label = customtkinter.CTkLabel(master=welcome_frame4, text="or", font=("Helvetica", 20, "bold"), text_color="#424242")
        #or_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        add_user_button = customtkinter.CTkButton(master=accounts_frame, text="add")
        add_user_button.configure(command=app.signup_window, corner_radius=0, cursor="hand2",
                                  width=180, height=30, text_color="#6B4CBF", hover_color="#141414", fg_color="#0A0A0A",
                                  font=("Helvetica", 20), image=add_user_icon)
        add_user_button.pack(pady=0)

        # Creating lists to store record names
        account_names = []
        filter_names = []

        # Selecting the record names from records table in database
        result2 = """SELECT username FROM users"""
        cursor.execute(result2)
        # Fetching each name one by one and storing it in button_name list
        for _ in result2:
            result3 = cursor.fetchone()
            account_names.append(result3)

        # Filtering out None values and adding non-None values to filter_names list.
        # Not sure why fetching all the names returns some None values.
        for i in account_names:
            if i != None:
                filter_names.append(i)

        # Creating buttons for each record entry in database
        for i in filter_names:
            button = customtkinter.CTkButton(master=accounts_frame, text=i[0])
            button.configure(command=lambda b=button: app.account_login_window(b), corner_radius=0, cursor="hand2", width=180, height=30, text_color="#294ec6", hover_color="#141414", fg_color="#0A0A0A", font=("Helvetica", 20), image=user_icon)
            button.pack(pady=0)

        # Printing names in filter_names to make sure the above function is working properly
        for i in filter_names:
            print(i[0], end=" | ")
        print()


    # Display sign up window
    def signup_window(self):

        global signup_username_entry
        global signup_password_entry

        # Create a frame in app window
        signup_frame = customtkinter.CTkFrame(master=app, width=600, height=520, fg_color="#141414", corner_radius=0)
        signup_frame.grid(row=0, column=0, columnspan=2, sticky="nesw")

        signup_frame2 = customtkinter.CTkFrame(master=signup_frame, width=600, height=520, fg_color="#141414", corner_radius=0)
        signup_frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        l3 = customtkinter.CTkLabel(master=signup_frame2, text="", image=profile_icon)
        l3.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        # Create a label to display text
        signup_label = customtkinter.CTkLabel(master=signup_frame2, text="Create account", font=("Helvetica", 30, "bold"))
        signup_label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        # Create entry box to type input
        signup_username_entry = customtkinter.CTkEntry(master=signup_frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Username")
        signup_username_entry.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

        signup_password_entry = customtkinter.CTkEntry(master=signup_frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password")
        signup_password_entry.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

        signup_button = customtkinter.CTkButton(master=signup_frame2, command=auth.signup, text="Sign up", fg_color="#294ec6", hover_color="#141414", corner_radius=30, cursor="hand2", width=200, height=50, border_width=3, border_color="#294ec6")
        signup_button.place(relx=0.5, rely=0.80, anchor=tkinter.CENTER)

        back_button = customtkinter.CTkButton(master=signup_frame, command=app.welcome_window, text="",
                                              fg_color="#141414",
                                              hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                              height=40, image=back_icon)
        back_button.place(x=20, y=20)

        random_password_button = customtkinter.CTkButton(master=signup_frame2, command=lambda: profile.generate_random_password(signup_frame2), text="",
                                              fg_color="#141414",
                                              hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                              height=45, image=random_icon)
        random_password_button.place(relx=0.244, rely=0.65, anchor=tkinter.CENTER)

        copy_button = customtkinter.CTkButton(master=signup_frame2, command=lambda: profile.copy_password(signup_frame), text="",
                                              fg_color="#141414",
                                              hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                              height=40, image=copy_icon)
        copy_button.place(relx=0.758, rely=0.65, anchor=tkinter.CENTER)

        left_divider_frame = customtkinter.CTkFrame(master=signup_frame, width=2, height=300, fg_color="#424242", corner_radius=0)
        left_divider_frame.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

        right_divider_frame = customtkinter.CTkFrame(master=signup_frame, width=2, height=300, fg_color="#424242", corner_radius=0)
        right_divider_frame.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)


    # Display log in window
    def account_login_window(self, b):

        global login_username_entry
        global login_password_entry
        global button_name
        global button_name4
        button_name = b.cget("text")

        login_frame = customtkinter.CTkFrame(master=app, width=600, height=520, fg_color="#141414", corner_radius=0)
        login_frame.grid(row=0, column=0, columnspan=2, sticky="nesw")
        login_frame.grid_rowconfigure(4, weight=1)

        login_frame2 = customtkinter.CTkFrame(master=login_frame, width=500, height=400, fg_color="#141414",
                                               corner_radius=0)
        login_frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        try:

            cursor.execute("SELECT profile_icon FROM users WHERE username=?", [button_name])
            result5 = cursor.fetchone()
            profile_img_icon = customtkinter.CTkImage(Image.open(result5[0]), size=(150, 150))
            l3 = customtkinter.CTkLabel(master=login_frame2, text="", image=profile_img_icon)
            l3.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        except:

            l3 = customtkinter.CTkLabel(master=login_frame2, text="", image=profile_icon)
            l3.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        #l3 = customtkinter.CTkLabel(master=login_frame2, text="", image=profile_icon)
        #l3.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        login_label = customtkinter.CTkLabel(master=login_frame2, text=button_name, font=("Helvetica", 30, "bold"))
        login_label.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)

        login_password_entry = customtkinter.CTkEntry(master=login_frame2, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password", show="*")
        login_password_entry.place(relx=0.5, rely=0.58, anchor=tkinter.CENTER)

        signup_label = customtkinter.CTkLabel(master=login_frame2, text="Don't have an account?", font=("Arial", 12))
        signup_label.place(relx=0.52, rely=0.66, anchor=tkinter.CENTER)

        signup_button = customtkinter.CTkButton(master=login_frame2, command=app.signup_window, text="Sign up", font=("Arial", 12, "underline"), text_color="#4182d6", fg_color="#141414", hover_color="#141414", cursor="hand2", width=40)
        signup_button.place(relx=0.71, rely=0.66, anchor=tkinter.CENTER)

        login_button = customtkinter.CTkButton(master=login_frame2, command=auth.account_login, text="Log in", fg_color="#294ec6", hover_color="#141414", corner_radius=30, cursor="hand2", width=200, height=50, border_width=3, border_color="#294ec6")
        login_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        back_button = customtkinter.CTkButton(master=login_frame, command=app.welcome_window, text="",
                                              fg_color="#141414",
                                              hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                              height=40, image=back_icon)
        back_button.place(x=20, y=20)

        left_divider_frame = customtkinter.CTkFrame(master=login_frame, width=2, height=300, fg_color="#424242", corner_radius=0)
        left_divider_frame.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

        right_divider_frame = customtkinter.CTkFrame(master=login_frame, width=2, height=300, fg_color="#424242", corner_radius=0)
        right_divider_frame.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

        button_name4 = button.cget("text")



    # Display frame when log in button is clicked
    def records_window(self):

        global add_login_frame
        global button2
        global records_frame
        global sidebar_frame



        sidebar_frame = customtkinter.CTkFrame(master=app, width=80, height=400, fg_color="#242424", corner_radius=0)
        sidebar_frame.grid(row=0, column=0, sticky="nesw")
        sidebar_frame.grid_rowconfigure(4, weight=1)

        try:

            cursor.execute("SELECT profile_icon FROM users WHERE username=?", [username])
            icon_label1 = cursor.fetchone()
            records_icon = customtkinter.CTkImage(Image.open(icon_label1[0]), size=(60, 60))
            icon_label = customtkinter.CTkLabel(master=sidebar_frame, text="", image=records_icon, bg_color="#242424")
            icon_label.grid(row=1, column=0, pady=10, sticky="n")

        except:

            icon_label = customtkinter.CTkLabel(master=sidebar_frame, text="", image=logo_icon, bg_color="#242424")
            icon_label.grid(row=1, column=0, pady=10, sticky="n")

        bar_label = customtkinter.CTkFrame(master=sidebar_frame, fg_color="#424242", width=60, height=3)
        bar_label.grid(row=2, column=0, sticky="n")

        add_button = customtkinter.CTkButton(master=sidebar_frame, command=app.create_record_window, text="", fg_color="#242424", hover_color="#424242", corner_radius=0, cursor="hand2", width=80, height=80, image=add_icon)
        add_button.grid(row=3, column=0, sticky="n")

        profile_button = customtkinter.CTkButton(master=sidebar_frame, command=profile.profile_window, text="",
                                                 image=profile_icon2,
                                                 fg_color="#242424", hover_color="#424242", height=80, width=80,
                                                 corner_radius=0, cursor="hand2")
        profile_button.grid(row=5, column=0, sticky="s")

        add_login_frame = customtkinter.CTkScrollableFrame(master=app, width=480, height=480, fg_color="#0A0A0A", corner_radius=0)
        add_login_frame.grid(row=0, column=1, columnspan=2, sticky="nesw")

        logout_button = customtkinter.CTkButton(master=sidebar_frame, command=app.welcome_window, text="", fg_color="#242424", hover_color="#424242", corner_radius=0, cursor="hand2", width=80, height=80, image=logout_icon)
        logout_button.grid(row=6, column=0, sticky="s")


        # Creating lists to store record names
        button_names = []
        filter_names = []

        # Selecting the record names from table of user that is logged in
        result2 = f"SELECT name FROM {username}"
        cursor.execute(result2)

        # Fetching each name from table one by one and storing it in button_name list
        for _ in result2:
            result3 = cursor.fetchone()
            button_names.append(result3)

        # Filtering out None values and adding non-None values to filter_names list.
        # Not sure why fetching all the names returns some None values.
        for i in button_names:
            if i != None:
                filter_names.append(i)

        # Creating buttons for each record in the table of the user that is logged in and displaying them
        for i in filter_names:

             button2 = customtkinter.CTkButton(master=add_login_frame, text=i[0], font=("Helvetica", 14, "bold"))
             button2.configure(command=lambda b=button2: records.record_authentication(b),
                             width=300,
                             height=50, fg_color="#6B4CBF", hover_color="#0A0A0A", corner_radius=30, cursor="hand2", border_width=3, border_color="#6B4CBF", image=lock_icon)
             button2.pack(pady=10)
            #3A5EFF
            #C17F4D

        for i in filter_names:
            print(i[0], end=" | ")
        print()


    # Display create record window
    def create_record_window(self):

        global record_name_entry
        global record_username_entry
        global record_password_entry
        global create_record_frame

        create_record_frame = customtkinter.CTkFrame(master=app, width=400, height=300, fg_color="#141414", bg_color="#0A0A0A", corner_radius=30)
        create_record_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        add_login_label = customtkinter.CTkLabel(master=create_record_frame, text="Create Record", font=("Helvetica", 30, "bold"))
        add_login_label.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)

        record_name_entry = customtkinter.CTkEntry(master=create_record_frame, width=260, height=30, fg_color="#2a2a2a",
                                                 placeholder_text="Record name")
        record_name_entry.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)

        record_username_entry = customtkinter.CTkEntry(master=create_record_frame, width=260, height=30, fg_color="#2a2a2a",
                                            placeholder_text="Username")
        record_username_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        record_password_entry = customtkinter.CTkEntry(master=create_record_frame, width=260, height=30, fg_color="#2a2a2a",
                                                 placeholder_text="Password")
        record_password_entry.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)

        create_login_button = customtkinter.CTkButton(master=create_record_frame, command=records.create_record, text="Create", fg_color="#294ec6", hover_color="#141414", corner_radius=30, cursor="hand2", width=200, height=50, border_width=3, border_color="#294ec6")
        create_login_button.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

        back_button = customtkinter.CTkButton(master=create_record_frame, command=records.destroy3, text="", fg_color="#141414",
                                                hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                                height=40, image=back_icon)
        back_button.place(x=20, y=20)


    # Display record window of record clicked
    def show_record_window(self, x, y, z):

        global show_record_frame

        show_record_frame = customtkinter.CTkFrame(master=app, width=500, height=400, fg_color="#141414", border_width=3,
                                        border_color="#424242", corner_radius=0)
        show_record_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        show_record_label = customtkinter.CTkLabel(master=show_record_frame, text=f"{z}",
                                                 font=("Helvetica", 30, "bold"))
        show_record_label.place(relx=0.5, rely=0.15, anchor="center")

        show_record_label2 = customtkinter.CTkLabel(master=show_record_frame, text="Username:", font=("Helvetica", 15, "bold"))
        show_record_label2.place(x=25, y=120)

        show_record_label2 = customtkinter.CTkLabel(master=show_record_frame, text="Password:",
                                                    font=("Helvetica", 15, "bold"))
        show_record_label2.place(x=25, y=180)

        record_password_entry = customtkinter.CTkEntry(master=show_record_frame, width=260, height=30, fg_color="#2a2a2a")
        record_password_entry.place(x=120, y=180)

        record_username_entry = customtkinter.CTkEntry(master=show_record_frame, width=260, height=30, fg_color="#2a2a2a")
        record_username_entry.place(x=120, y=120)

        back_button = customtkinter.CTkButton(master=show_record_frame, command=records.destroy2, text="", fg_color="#141414",
                                               hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                               height=40, image=back_icon)
        back_button.place(x=20, y=20)

        copy_username_button = customtkinter.CTkButton(master=show_record_frame,
                                                       command=lambda: records.copy_username(record_username_entry), text="",
                                                       fg_color="#141414", hover_color="#242424", corner_radius=6,
                                                       cursor="hand2", width=40, height=40, image=copy_icon)
        copy_username_button.place(x=390, y=115)

        copy_password_button = customtkinter.CTkButton(master=show_record_frame, command=lambda: records.copy_password(record_password_entry), text="",
                                              fg_color="#141414", hover_color="#242424", corner_radius=6,
                                              cursor="hand2", width=40, height=40, image=copy_icon)
        copy_password_button.place(x=390, y=175)

        edit_button = customtkinter.CTkButton(master=show_record_frame, command=lambda: records.edit_record(record_username_entry, record_password_entry), text="", fg_color="#141414", hover_color="#242424",
                                              corner_radius=6, cursor="hand2", width=40, height=40, image=edit_icon)
        edit_button.place(x=435, y=20)

        delete_button = customtkinter.CTkButton(master=show_record_frame, command=records.delete_record, text="",
                                                fg_color="#141414", hover_color="#242424", corner_radius=0,
                                                cursor="hand2", width=494, height=60, image=delete_icon)
        delete_button.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

        # Inserting password into the password entry box
        record_username_entry.configure(state="normal")
        record_username_entry.insert(0, x[0])
        record_username_entry.configure(state="disabled")
        record_password_entry.configure(state="normal")
        record_password_entry.insert(0, y[0])
        record_password_entry.configure(state="disabled")


    # Display welcome window - "logout"
    def logout(self):

        app.welcome_window()


class Records():

    def record_authentication(self, b):

        #global result
        #global button_name
        global authentication_entry
        global authentication_frame
        global button_name2

        button_name = b.cget("text")
        cursor.execute(f"SELECT username FROM {username} WHERE name=?", [button_name])
        result = cursor.fetchone()
        cursor.execute(f"SELECT password FROM {username} WHERE name=?", [button_name])
        result2 = cursor.fetchone()
        button_name2 = button_name

        authentication_frame = customtkinter.CTkFrame(master=app, width=400, height=200, fg_color="#141414", bg_color="#0A0A0A", corner_radius=30)
        authentication_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        authentication_entry = customtkinter.CTkEntry(master=authentication_frame, width=260, height=30, fg_color="#2a2a2a", placeholder_text="Password", show="*")
        authentication_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        key_button = customtkinter.CTkLabel(master=authentication_frame, text="", image=key_icon)
        key_button.place(relx=0.10, rely=0.5, anchor=tkinter.CENTER)

        show_record_label = customtkinter.CTkLabel(master=authentication_frame, text=f"Enter Password:",
                                                   font=("Helvetica", 20, "bold"))
        show_record_label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        auth_button = customtkinter.CTkButton(master=authentication_frame, command=lambda: auth.verify(result, result2, button_name), text="",
                                               fg_color="#294ec6", hover_color="#141414", corner_radius=30,
                                               cursor="hand2", width=160, height=40, border_width=3,
                                               border_color="#294ec6", image=enter_icon)
        auth_button.place(relx=0.5, rely=0.77, anchor=tkinter.CENTER)

        back_button = customtkinter.CTkButton(master=authentication_frame, command=records.destroy, text="",
                                              fg_color="#141414",
                                              hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                              height=40, image=back_icon)
        back_button.place(x=20, y=20)



    # Creates a record from inputs
    def create_record(self):

        global name
        global username1
        global password1
        global button
        # Getting name and password entries from create_record_window
        name = record_name_entry.get()
        username1 = record_username_entry.get()
        password1 = record_password_entry.get()
        if name != "" and username1 != "" and password1 != "":
            if len(name) <= 15:
                # Inserting name and password into table of user that is logged in
                cursor.execute(f"INSERT INTO {username} VALUES (?, ?, ?)", [name, username1, password1])
                conn.commit()
                # Show that record has been created
                messagebox.showinfo("Success", f"{name} record added")
                # Go back to records_window when record has been created
                app.records_window()
            else:
                messagebox.showerror("Error", "Name may not exceed 15 characters.")
        else:
            messagebox.showerror("Error", "Enter all data.")



    # Deletes specified login
    def delete_record(self):

        # Delete record where name = button_name
        cursor.execute(f"""DELETE FROM {username} WHERE name=?""", [button_name2])
        conn.commit()
        messagebox.showinfo("Deleted", f"Record deleted.")
        app.records_window()


    # Editing username and password in record
    def edit_record(self, x, y):


        edit_frame = customtkinter.CTkFrame(master=show_record_frame, width=350, height=250, fg_color="#141414", border_width=3, corner_radius=0, border_color="#424242")
        edit_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        back_button = customtkinter.CTkButton(master=edit_frame, command=edit_frame.destroy, text="",
                                              fg_color="#141414",
                                              hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                              height=40, image=back_icon)
        back_button.place(x=20, y=20)

        edit_record_entry1 = customtkinter.CTkEntry(master=edit_frame, width=200, height=30,
                                                       fg_color="#2a2a2a", placeholder_text="Username")
        edit_record_entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        edit_record_entry2 = customtkinter.CTkEntry(master=edit_frame, width=200, height=30,
                                                       fg_color="#2a2a2a", placeholder_text="Password")
        edit_record_entry2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        edit_record_label = customtkinter.CTkLabel(master=edit_frame, text=f"Edit",
                                                   font=("Helvetica", 30, "bold"))
        edit_record_label.place(relx=0.5, rely=0.17, anchor=tkinter.CENTER)

        edit_record_label2 = customtkinter.CTkLabel(master=edit_frame, text="",
                                                   font=("Helvetica", 30, "bold"), image=edit_icon2)
        edit_record_label2.place(relx=0.65, rely=0.17, anchor=tkinter.CENTER)

        show_record_label2 = customtkinter.CTkLabel(master=edit_frame, text="New:",
                                                    font=("Helvetica", 15, "bold"))
        show_record_label2.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)

        show_record_label2 = customtkinter.CTkLabel(master=edit_frame, text="New:",
                                                    font=("Helvetica", 15, "bold"))
        show_record_label2.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)

        global save_button
        # Setting password entrybox to normal so that you can edit it. It was disabled before so that you couldn't edit it.
        x.configure(state="normal")
        y.configure(state="normal")
        # Once edit button is clicked it creates a new button called "save", click the save button and it will save the changes. aka, make the entry -
        # box disabled again and updating the record in database
        save_button = customtkinter.CTkButton(master=edit_frame, command=lambda: records.save(x, y, edit_frame, edit_record_entry1, edit_record_entry2), text="",
                                                fg_color="#141414", hover_color="#242424", corner_radius=0,
                                                cursor="hand2", width=344, height=60, image=save_icon)
        save_button.place(relx=0.5, rely=0.87, anchor=tkinter.CENTER)


    def save(self, x, y, z, a, b):

        # Get the new edited username and password
        username2 = x.get()
        password2 = y.get()
        new_username = a.get()
        new_password = b.get()
        print(f"old username: {username2}")
        print(f"old password: {password2}")
        print(f"new password: {new_username}")
        print(f"new password: {new_password}")
        x.delete(0, len(username2))
        y.delete(0, len(password2))
        x.insert(0, new_username)
        y.insert(0, new_password)
        print(button_name2)
        # Set the entrybox to disabled again, so you can't edit it
        x.configure(state="disabled")
        y.configure(state="disabled")
        # Update that username and password in the database to resemble the new edited username and password
        cursor.execute(f"UPDATE {username} SET username=?, password=? WHERE name=?", [new_username, new_password, button_name2])
        conn.commit()
        #save_button.destroy()
        z.destroy()

        messagebox.showinfo("Saved", "Changes saved.")

    def copy_username(self, x):

        copy_password = x.get()
        # Clearing the clipboard
        app.clipboard_clear()
        # Copying record password to clipboard
        app.clipboard_append(copy_password)
        # Create label to display that password has been copied
        copy_label = customtkinter.CTkLabel(master=show_record_frame, text="Copied!", font=("Helvetica", 12),
                                            fg_color="#141414")
        copy_label.place(x=390, y=150)

    # Copy record password to clipboard
    def copy_password(self, x):
        copy_password = x.get()
        # Clearing the clipboard
        app.clipboard_clear()
        # Copying record password to clipboard
        app.clipboard_append(copy_password)
        # Create label to display that password has been copied
        copy_label = customtkinter.CTkLabel(master=show_record_frame, text="Copied!", font=("Helvetica", 12), fg_color="#141414")
        copy_label.place(x=390, y=210)


    def destroy(self):

        authentication_frame.destroy()

    def destroy2(self):

        authentication_frame.destroy()
        show_record_frame.destroy()

    def destroy3(self):
        create_record_frame.destroy()


class Profile():

    def profile_image(self, x, y):

        global img_icon

        # open an image ending with .png or .jpg
        file = askopenfile(parent=x, mode="rb", title="Choose a file", filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg")])
        if file is not None:
            print("file was successful")

            name = file.name
            name2 = os.path.basename(file.name)
            print(name)
            print(name2)

            #print(directory)
            print(name)
            # convert to RGB
            img = Image.open(f"{name}").convert("RGB")
            # convert to numpy array
            arrImg = np.array(img)
            # create a new image with alpha channel
            alph = Image.new('L', img.size, 0)
            # create a draw object
            draw = ImageDraw.Draw(alph)
            # create a circle
            draw.pieslice([0, 0, img.size[0], img.size[1]], 0, 360, fill=255)
            # convert to numpy array
            arAlpha = np.array(alph)
            # add alpha channel to the image
            arrImg = np.dstack((arrImg, arAlpha))
            # save the resulting image
            Image.fromarray(arrImg).save(f"profile_images/{name2}")

            saved_img = f"profile_images/{name2}"

            test_img = Image.open(saved_img)
            img_resize = test_img.resize((180, 180), Image.Resampling.LANCZOS)
            img_resize.save(saved_img)
            img_icon = customtkinter.CTkImage(Image.open(saved_img), size=(180, 180))



            cursor.execute("UPDATE users SET profile_icon=? WHERE username=?", [saved_img, username])
            conn.commit()

            l4 = customtkinter.CTkLabel(master=y, text="", image=img_icon, corner_radius=100)
            l4.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        #y.configure(image=img_icon)

    def profile_window(self):

        global profile_img_icon

        #img_icon2 = customtkinter.CTkImage(Image.open("images/profileimg.png"), size=(25, 25))

        profile_window_frame = customtkinter.CTkFrame(master=app, width=600, height=520, fg_color="#141414", corner_radius=0)
        profile_window_frame.grid(row=0, column=0, columnspan=2, sticky="nesw")

        profile_frame = customtkinter.CTkFrame(master=profile_window_frame, width=600, height=520, fg_color="#141414", corner_radius=0)
        profile_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        try:

            cursor.execute("SELECT profile_icon FROM users WHERE username=?", [username])
            result = cursor.fetchone()
            profile_img_icon = customtkinter.CTkImage(Image.open(result[0]), size=(180, 180))
            l3 = customtkinter.CTkLabel(master=profile_frame, text="", image=profile_img_icon)
            l3.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        except:

            profile_img_icon1 = customtkinter.CTkImage(Image.open("images/profile_icon1.png"), size=(220, 220))
            l3 = customtkinter.CTkLabel(master=profile_frame, text="", image=profile_img_icon1)
            l3.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

        photo_button = customtkinter.CTkButton(master=profile_frame, command=lambda: profile.profile_image(profile_frame, profile_frame), text="",
                                              fg_color="#141414", bg_color="#141414", hover_color="#242424",
                                              corner_radius=6, cursor="hand2", width=30, height=40, image=photo_icon)
        photo_button.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

        back_button = customtkinter.CTkButton(master=profile_window_frame, command=app.records_window, text="",
                                              fg_color="#141414",
                                              hover_color="#242424", corner_radius=6, cursor="hand2", width=40,
                                              height=40, image=back_icon)
        back_button.place(x=20, y=20)

        delete_button = customtkinter.CTkButton(master=app, command=auth.delete_account, text="",
                                                fg_color="#141414", hover_color="#242424", corner_radius=0,
                                                cursor="hand2", width=494, height=60, image=delete_icon)
        delete_button.grid(row=0, column=0, columnspan=2, sticky="sew")

        profile_username_label = customtkinter.CTkLabel(master=profile_frame, text="Username:",
                                                    font=("Helvetica", 15, "bold"))
        profile_username_label.place(relx=0.25, rely=0.55, anchor=tkinter.CENTER)

        profile_password_label = customtkinter.CTkLabel(master=profile_frame, text="Password:",
                                                    font=("Helvetica", 15, "bold"))
        profile_password_label.place(relx=0.25, rely=0.65, anchor=tkinter.CENTER)

        record_username_entry = customtkinter.CTkEntry(master=profile_frame, width=260, height=30,
                                                       fg_color="#2a2a2a")
        record_username_entry.place(relx=0.55, rely=0.55, anchor=tkinter.CENTER)

        record_password_entry = customtkinter.CTkEntry(master=profile_frame, width=260, height=30,
                                                       fg_color="#2a2a2a")
        record_password_entry.place(relx=0.55, rely=0.65, anchor=tkinter.CENTER)

        edit_button = customtkinter.CTkButton(master=app, text="",
                                              fg_color="#141414", hover_color="#242424", bg_color="#141414",
                                              corner_radius=6, cursor="hand2", width=40, height=40, image=edit_icon2)
        edit_button.grid(row=0, column=1, pady=20, padx=20, sticky="ne")

        cursor.execute(f"SELECT username FROM users WHERE username=?", [username])
        profile_username = cursor.fetchone()
        record_username_entry.insert(0, profile_username)
        record_username_entry.configure(state="disabled")

        profile_password = ""
        for _ in password:
            profile_password = profile_password + "*"

        record_password_entry.insert(0, profile_password)
        record_password_entry.configure(state="disabled")


    def generate_random_password(self, x):

        signup_password_entry.delete(0, 20)
        # gather our characters
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = lower.upper()
        symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
        numbers = "1234567890"
        all = lower + upper + symbols + numbers

        # set password length
        length = 20

        # loop through each character
        password = ""
        for _ in range(length):
            password = "".join([password, random.choice(all)])

        signup_password_entry.insert(0, password)

        signup_copy_label = customtkinter.CTkLabel(master=x, text="Make sure to copy the password!", font=("Arial", 12), fg_color="#141414", text_color="#BF4541")
        signup_copy_label.place(relx=0.43, rely=0.71, anchor=tkinter.CENTER)


    def copy_password(self, x):

            copy_password = signup_password_entry.get()
            # Clearing the clipboard
            app.clipboard_clear()
            # Copying record password to clipboard
            app.clipboard_append(copy_password)
            # Create label to display that password has been copied
            copy_label = customtkinter.CTkLabel(master=x, text="Copied!", font=("Helvetica", 12),
                                                fg_color="#141414")
            copy_label.place(relx=0.758, rely=0.7, anchor=tkinter.CENTER)

class Authentication():

    # Storing user data into database
    def signup(self):

        username = signup_username_entry.get()
        password = signup_password_entry.get()
        # If username or password entries are emtpy, display error
        if username != "" and password != "":
            # If username contains anything else other than letters, display error
            if username.isalpha():
                # Selecting usernames from database, if the username already exists in the database, display error
                cursor.execute("SELECT username FROM users WHERE username=?", [username])
                if cursor.fetchone() is not None:
                    messagebox.showerror("Error", "Username already exists.")
                else:
                    # Hashing the password
                    encoded_password = password.encode("utf-8")
                    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                    # Print hashed password to make sure password is being hashed correctly
                    print(hashed_password)
                    # Storing the username and hashed password into the database
                    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", [username, hashed_password, ""])
                    conn.commit()
                    messagebox.showinfo("Success", "Account created.")
                    # Create table in database for this user to store their records
                    cursor.execute(f"""
                        CREATE TABLE IF NOT EXISTS {username} (
                            name TEXT NOT NULL,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL
                    )
                    """)
                    # Go back to welcome_window so that you can log into the account
                    app.welcome_window()
            else:
                messagebox.showerror("Error", "Username may only contain letters.")
        else:
            messagebox.showerror("Error", "Enter all data.")


    def account_login(self):

        global username
        global password
        username = button_name
        password = login_password_entry.get()
        if username != "" and password != "":
            # Fetching username and password from database
            cursor.execute("SELECT password FROM users WHERE username=?", [username])
            result = cursor.fetchone()
            if result:
                # Checking if username and password entered matches username and password in database
                if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                    # Display records_window is login is successful
                    app.records_window()
                else:
                    messagebox.showerror("Error", "Invalid login.")
            else:
                messagebox.showerror("Error", "Invalid login.")
        else:
            messagebox.showerror("Error", "Enter password.")

    def verify(self, x, y, z):
        print(button_name)
        if authentication_entry.get() == password:
            app.show_record_window(x, y, z)
        else:
            messagebox.showerror("Error", "Incorrect password.")

    def delete_account(self):
        print(button_name4)
        cursor.execute("DELETE FROM users where username=?", [button_name4])
        conn.commit()
        cursor.execute(f"DROP TABLE {username}")
        conn.commit()
        messagebox.showinfo("Success", "Account deleted.")
        app.welcome_window()


if __name__ == "__main__":
    app = App()
    records = Records()
    profile = Profile()
    auth = Authentication()
    app.app_properties()
    app.welcome_window()
    app.mainloop()

