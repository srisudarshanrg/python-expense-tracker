import customtkinter as c
from tkinter import *
import psycopg2 as pg
from tkinter import messagebox as mb
from werkzeug.security import generate_password_hash, check_password_hash

# authentication functions
def Authenticate():
    username_entered = str(username_entered_entry.get())
    password_entered = str(password_entered_entry.get())

    get_username_query = str("SELECT * FROM login_details WHERE username=%s and password=%s")
    cursor.execute(get_username_query, (username_entered,password_entered))

    number_affected = cursor.rowcount
    if number_affected == 0:
        mb.showerror("Incorrect Credentials", "The username or password you have entered is incorrect")
    else:
        import expense_tracker

    print(number_affected)

def open_sign_up():
    root.destroy()
    import sign_up

# setting up database connection
conn = pg.connect(host="localhost", dbname="idp", user="postgres", password="raptor3796", port=5432)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS login_details (
        id INT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR
    );
""")

conn.commit()

# gui
c.set_appearance_mode("system")
c.set_default_color_theme("blue")

root = c.CTk()
root.title("Raptor Expense Tracker")
root.geometry("500x340")
root.resizable(0, 0)

# create widgets
c.CTkLabel(root, text="Raptor Expense Tracker", font=("Arial", 25)).grid(row=0, column=0, columnspan=2, pady=20)

c.CTkLabel(root, text="Enter username", font=("Arial", 25)).grid(row=1, column=0, pady=15, padx=10)
username_entered_entry = Entry(root,background="#383838", relief="flat", foreground="#fff", cursor="xterm #fff", font=("Arial", 25))
username_entered_entry.grid(row=1, column=1, padx=10, pady=15)

c.CTkLabel(root, text="Enter password", font=("Arial", 25)).grid(row=2, column=0, pady=15, padx=10)
password_entered_entry = Entry(root, background="#383838", relief="flat", foreground="#fff", font=("Arial", 25))
password_entered_entry.grid(row=2, column=1, padx=10, pady=15)

enter_button = c.CTkButton(root, text="Enter", font=("Arial", 25), width=200, command=Authenticate)
enter_button.grid(row=3, column=0, columnspan=2, pady=20)

sign_up_button = c.CTkButton(root, text="Sign Up", font=("Arial", 25), width=200, command=open_sign_up)
sign_up_button.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()