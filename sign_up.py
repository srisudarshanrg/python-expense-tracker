import customtkinter as c
from tkinter import *
import psycopg2 as pg
from tkinter import messagebox as mb
from werkzeug.security import generate_password_hash

# setting up database connection
conn = pg.connect(host="localhost", dbname="idp", user="postgres", password="raptor3796", port=5432)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS login_details (
        id INT PRIMARY KEY,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR NOT NULL
    );
""")

conn.commit()

# authentication functions
def SignUp():
    # get entered credentials
    username = str(username_entered_entry.get())
    password = str(password_entered_entry.get())
    confirm_password = str(password_entered_confirm.get())

    # check if username already exists
    check_username_exists_query = "SELECT * FROM login_details where username=%s"
    cursor.execute(check_username_exists_query, (username,))
    
    existing_rows = cursor.fetchall()
    if len(existing_rows) > 0 :
        mb.showerror("Existing Username", "This username already exists. Choose another one")

    if password != confirm_password:
        mb.showerror("Confirm Password", "Your password and confirmed password don't match")
        password_entered_entry.delete(1.0, END)
        password_entered_confirm.delete(1.0, END)
        return
    
    # hashing password for security
    hashed_password = generate_password_hash(password, "scrypt", 10)
    
    # get latest id
    get_latest_id_query = "SELECT COUNT(*) FROM login_details"
    cursor.execute(get_latest_id_query)

    row_count = cursor.fetchone()[0]
    latest_id = row_count + 1

    # adding user to database
    add_user_query = "INSERT INTO login_details(id, username, password) values(%s, %s, %s)"
    cursor.execute(add_user_query, (latest_id, username, hashed_password))
    conn.commit()
    mb.showinfo("User Added", f"You have been signed into Raptor Expenses as {username}")
    root.destroy()
    import login

def open_login():
    root.destroy()
    import login

# gui
c.set_appearance_mode("system")
c.set_default_color_theme("blue")

root = c.CTk()
root.title("Raptor Expense Tracker")
root.geometry("550x340")
root.resizable(0, 0)

# create widgets
c.CTkLabel(root, text="Raptor Expense Tracker", font=("Arial", 25)).grid(row=0, column=0, columnspan=2, pady=20)

c.CTkLabel(root, text="Enter username", font=("Arial", 25)).grid(row=1, column=0, pady=15, padx=10)
username_entered_entry = Entry(root,background="#383838", relief="flat", cursor="xterm #fff", font=("Arial", 25))
username_entered_entry.grid(row=1, column=1, padx=10, pady=15)

c.CTkLabel(root, text="Enter password", font=("Arial", 25)).grid(row=2, column=0, pady=15, padx=10)
password_entered_entry = Entry(root, background="#383838", relief="flat", font=("Arial", 25))
password_entered_entry.grid(row=2, column=1, padx=10, pady=15)

c.CTkLabel(root, text="Confirm password", font=("Arial", 25)).grid(row=3, column=0, pady=15, padx=10)
password_entered_confirm = Entry(root, background="#383838", relief="flat", font=("Arial", 25))
password_entered_confirm.grid(row=3, column=1, padx=10, pady=15)

sign_up_button = c.CTkButton(root, text="Sign Up", font=("Arial", 25), width=200, command=SignUp)
sign_up_button.grid(row=4, column=0, columnspan=2, pady=5)

login_button = c.CTkButton(root, text="Login", font=("Arial", 25), width=200, command=open_login)
login_button.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()