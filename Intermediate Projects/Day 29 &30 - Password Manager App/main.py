from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    generated = pw_numbers + pw_symbols + pw_letters
    shuffle(generated)
    random_password = "".join(generated)

    pass_input.delete(0, END)
    pass_input.insert(0, f"{random_password}")
    copy(f"{random_password}")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_entry = web_input.get().title()
    try:
        with open("data.json", "r") as records:
            entries = json.load(records)
    except FileNotFoundError:
        messagebox.showinfo(title=website_entry, message=f"No Data File Found.")
    else:
        if website_entry in entries:
            load_email = entries[website_entry]["email"]
            load_password = entries[website_entry]["password"]
            copy(f"{load_password}")
            messagebox.showinfo(title=website_entry, message=f"Email/User: {load_email}\nPassword: {load_password}"
                                                             f"\n\nPassword copied to clipboard!")
        else:
            messagebox.showinfo(title=website_entry, message=f"No details for this website exists.")
# ALTERNATIVE: (not recommended for can be easily done using if-else)
    #   try:
    #     load_email = entries[website_entry]["email"]
    #     load_password = entries[website_entry]["password"]
    #   except KeyError:
    #     messagebox.showinfo(title=website_entry, message=f"No details for this website exists.")
    #   else:
    #     copy(f"{load_password}")
    #     messagebox.showinfo(title=website_entry, message=f"Email/User: {load_email}\nPassword: {load_password}"
    #                                                      f"\n\nPassword copied to clipboard!")
    #   finally:
    #     web_input.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = web_input.get().title()
    email_entry = email_input.get()
    password_entry = pass_input.get()
# NEW DATA FORMAT
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": password_entry,
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0 or len(email_entry) <= 10:
        messagebox.showinfo(title="Yikes! :(", message="You left a field empty!")
    else:
        try:
            with open("data.json", "r") as records:
                entries = json.load(records)
        except FileNotFoundError:
            with open("data.json", "w") as records:
                json.dump(new_data, records, indent=4)
        else:
            entries.update(new_data)
            with open("data.json", "w") as records:
                json.dump(entries, records, indent=4)
        finally:
            web_input.delete(0, END)
            email_input.delete(0, len(email_entry) - 10)
            pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager by <cln.py>")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
emailuser = Label(text="Email/Username:")
emailuser.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry
web_input = Entry(width=33)
web_input.grid(column=1, row=1)
web_input.focus()
email_input = Entry(width=52)
email_input.insert(0, "@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)
pass_input = Entry(width=33)
pass_input.grid(column=1, row=3)

# Buttons
gen_pw = Button(text="Generate Password", command=generate_password)
gen_pw.grid(column=2, row=3)
add_pw = Button(text="Add", width=43, command=save)
add_pw.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)

window.mainloop()
