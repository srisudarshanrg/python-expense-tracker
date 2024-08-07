import customtkinter as c
from tkinter import *
import psycopg2

# setting up database connection
conn = psycopg2.connect(host="localhost", dbname="idp", user="postgres", password="raptor3796", port=5432)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS login_details (
        id INT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR
    );
""")

conn.commit()
cursor.close()
conn.close()


c.set_appearance_mode("system")
c.set_default_color_theme("blue")

root = c.CTk()
root.title("Raptor Expense Tracker")
root.geometry("500x340")
# root.resizable(0, 0)

# create widgets
c.CTkLabel(root, text="Raptor Expense Tracker", font=("Arial", 25)).grid(row=0, column=0, columnspan=2, pady=20)

c.CTkLabel(root, text="Enter username", font=("Arial", 25)).grid(row=1, column=0, pady=15, padx=10)
username_entered = Entry(root,background="#383838", relief="flat", foreground="#fff", cursor="xterm #fff", font=("Arial", 25))
username_entered.grid(row=1, column=1, padx=10, pady=15)

c.CTkLabel(root, text="Enter password", font=("Arial", 25)).grid(row=2, column=0, pady=15, padx=10)
password_entered = Entry(root, background="#383838", relief="flat", foreground="#fff", font=("Arial", 25))
password_entered.grid(row=2, column=1, padx=10, pady=15)

enter_button = c.CTkButton(root, text="Enter", font=("Arial", 25), width=200)
enter_button.grid(row=3, column=0, columnspan=2, pady=20)

sign_up_button = c.CTkButton(root, text="Sign Up", font=("Arial", 25), width=200)
sign_up_button.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()