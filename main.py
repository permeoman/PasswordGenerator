from tkinter import *
import random


# _____________________________________password generator_______________________________________#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 10)
    nr_numbers = random.randint(4, 6)
    nr_symbols = random.randint(3, 6)

    rand_letters = [random.choice(letters) for char in range(nr_letters)]
    rand_numbers = [random.choice(numbers) for num in range(nr_numbers)]
    rand_symbols = [random.choice(symbols) for sym in range(nr_symbols)]

    password_list = rand_letters + rand_numbers + rand_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

# ______________________________________UI SETUP ________________________________________________#

window = Tk()
window.title("Password Generator")
window.minsize(width=400, height=300)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="img.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1, padx=5, pady=5)
email_entry = Entry(width=20)
email_entry.grid(column=1, row=2, padx=5, pady=5)
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, padx=5, pady=5)


# Buttons
gen_password = Button(text="Generate Password", width=20)
gen_password.grid(column=2, row=3)
add_password = Button(text="Add Password", width=20)
add_password.grid(column=1, row=4)
search = Button(text="Search", width=20)
search.grid(column=2, row=1)
window.mainloop()

